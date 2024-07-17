from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}

def read_csv(file_path):
    try:
        products = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        return {"error": str(e)}

def read_sqlite(db_path, product_id=None):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if product_id:
            cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        if not rows:
            return {"error": "Product not found"}
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite('products.db', product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if 'error' in data:
        return render_template('product_display.html', error=data['error'])

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
