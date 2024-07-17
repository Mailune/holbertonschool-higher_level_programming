from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if 'error' in data:
        return render_template('product_display.html', error=data['error'])

    if product_id:
        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
