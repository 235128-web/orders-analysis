import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers VALUES
(1, 'Ali', 'Islamabad'),
(2, 'Sara', 'Lahore'),
(3, 'Bilal', 'Karachi'),
(4, 'Ayesha', 'Islamabad'),
(5, 'Usman', 'Lahore'),
(6, 'Hina', 'Karachi');
INSERT INTO orders VALUES
(1, 1, 4500),
(2, 1, 7200),
(3, 2, 3000),
(4, 2, 8600),
(5, 3, 2000),
(6, 3, 1500),
(7, 4, 9800),
(8, 5, 5000),
(9, 5, 6000),
(10, 6, 3000);
""")
conn.commit()
conn.close()
print("Database created.")