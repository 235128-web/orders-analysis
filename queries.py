import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

print("Part a - Customer orders (joined):")
cur.execute("""
SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
""")
for row in cur.fetchall():
    print(row)

print("Part b - Total spend per customer:")
cur.execute("""
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC;
""")
for row in cur.fetchall():
    print(row)

print("Part c - Cities with avg order > 5000:")
cur.execute("""
SELECT c.city, AVG(o.amount) AS avg_order
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING AVG(o.amount) > 5000;
""")
for row in cur.fetchall():
    print(row)

conn.close()