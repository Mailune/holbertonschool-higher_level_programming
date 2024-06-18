-- script that creates a table in the current database
USE hbtn_0c_0;

-- Check if the table exists first
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
