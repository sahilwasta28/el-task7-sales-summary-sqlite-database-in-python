import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connecting to the database
conn = sqlite3.connect("sales_data.db")

# Displaying all record in the database 
df = pd.read_sql_query("SELECT * FROM sales", conn)
print(df)

# --- Query 1: Revenue & Quantity per Product ---
query1 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df1 = pd.read_sql_query(query1, conn)
print("\nQuery 1: Revenue & Quantity per Product\n")
print(df1)

# --- Query 2: Total Revenue of All Products ---
query2 = "SELECT SUM(quantity * price) AS total_revenue FROM sales"
df2 = pd.read_sql_query(query2, conn)
print("\nQuery 2: Total Revenue (All Products)\n")
print(df2)

# --- Query 3: Top Selling Product by Revenue ---
query3 = """
SELECT product, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 1
"""
df3 = pd.read_sql_query(query3, conn)
print("\nQuery 3: Top Selling Product by Revenue\n")
print(df3)

# --- Query 4: Average Price per Product ---
query4 = """
SELECT product, AVG(price) AS avg_price
FROM sales
GROUP BY product
"""
df4 = pd.read_sql_query(query4, conn)
print("\nQuery 4: Average Price per Product\n")
print(df4)

# Closing the connection
conn.close()

# Plot 1: Revenue by Product
df1.plot(kind="bar", x="product", y="revenue", legend=False, color="skyblue")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart_revenue.png")
plt.show()

# Plot 2: Quantity Sold by Product
df1.plot(kind="bar", x="product", y="total_qty", legend=False, color="lightgreen")
plt.ylabel("Quantity Sold")
plt.title("Quantity Sold by Product")
plt.tight_layout()
plt.savefig("sales_chart_quantity.png")
plt.show()
