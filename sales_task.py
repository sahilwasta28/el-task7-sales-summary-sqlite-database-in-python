import sqlite3

# Connecting to the database (creating file if it doesn't exists) 
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Inserting some sample data in the table 
sample_data = [
    ("Apples", 10, 2.5),
    ("Bananas", 5, 1.0),
    ("Apples", 4, 2.5),
    ("Oranges", 8, 3.0),
    ("Bananas", 7, 1.0),
    ("Mangoes",12,3.5),
    ("Mangoes",10,5.5),
    ("Papaya",6,4.0),
    ("Apples", 15, 2.5),
    ("Bananas", 9, 1.0),
    ("Oranges", 6, 3.0),
    ("Mangoes", 8, 4.0),
    ("Papaya", 10, 4.5),
    ("Grapes", 12, 3.2),
    ("Watermelon", 5, 6.0),
    ("Pineapple", 4, 5.5),
    ("Kiwi", 7, 6.5),
    ("Guava", 14, 2.8),
    ("Apples", 11, 2.5),
    ("Bananas", 15, 1.0),
    ("Oranges", 10, 3.0),
    ("Mangoes", 14, 4.5),
    ("Papaya", 8, 4.0),
    ("Grapes", 10, 3.0),
    ("Watermelon", 7, 5.5),
    ("Pineapple", 6, 5.0),
    ("Kiwi", 9, 6.0),
    ("Guava", 13, 2.5),
    ("Apples", 9, 2.5),
    ("Bananas", 6, 1.0),
    ("Oranges", 12, 3.0),
    ("Mangoes", 9, 5.0),
    ("Papaya", 11, 4.2),
    ("Grapes", 8, 3.5),
    ("Watermelon", 6, 5.8),
    ("Pineapple", 9, 5.3),
    ("Kiwi", 5, 6.5),
    ("Guava", 10, 2.9),
    ("Apples", 8, 2.5),
    ("Bananas", 13, 1.0),
    ("Oranges", 9, 3.0),
    ("Mangoes", 7, 4.8),
    ("Papaya", 13, 4.1),
    ("Grapes", 11, 3.4),
    ("Watermelon", 8, 6.2),
    ("Pineapple", 10, 5.6),
    ("Kiwi", 6, 6.3),
    ("Guava", 12, 2.7),
    ("Apples", 7, 2.5),
    ("Bananas", 8, 1.0)
]

cursor.executemany(
    "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
    sample_data
)

# Saving the changes
conn.commit()
conn.close()

print("Database created and sample data inserted.")