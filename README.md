📂 **Elevate Labs Data Analyst Internship – Task 7: Sales Database Creation & Analysis**

📌 **Task Overview**  
This task, completed as part of the Elevate Labs Data Analyst Internship, focuses on creating a structured sales database, inserting sample records, and analyzing sales performance using SQLite queries.  
The goal was to simulate a real-world product sales environment, calculate revenues, and identify high-performing products for business decision-making.

---

⚙️ **Tools and Dataset**  
**Tools:** SQLite (via Python `sqlite3`), DB Browser for SQLite, Matplotlib (for visualizations)  
**Dataset:** `sales_data.db` (Sales table with columns: `id`, `product`, `quantity`, `price`)

---

📝 **Steps and Analysis**  

1. **Database Setup:**  
   - Created a SQLite database named `sales_data.db`.  
   - Defined a `sales` table with columns for product name, quantity sold, and unit price.  

2. **Data Insertion:**  
   - Added initial sample sales records.   

3. **SQL Queries Performed:**  
   - Retrieved all records from the database for validation.  
   - Calculated **total quantity sold** and **total revenue** per product using `GROUP BY`.  
   - Sorted results to identify the **top-performing products**.  

4. **Visualization:**  
   - Created a bar chart showing product-wise revenue and sales to visually compare performance.  

---

🔍 **Key Insights and Conclusions**  
- **Mangoes** are the clear top revenue driver and also lead in units sold.
- **Papaya** and **Apples** follow next in revenue; Papaya edges Oranges despite similar quantities—indicating a higher unit price.
- **High-price, low-quantity products** (especially **Kiwi**, **Pineapple** and **Watermelon**) generate solid revenue; Kiwi shows the **highest revenue per unit**.
- **Bananas** sell in high volume but deliver the **lowest revenue**, reflecting their low unit price.
  
---

🙋‍♂️ **Author**  
**Name:** Sahil Wasta  
**Internship Task:** Task 7 – Sales Database Creation & Analysis  
**Tools Used:** SQLite, Python, Matplotlib  
