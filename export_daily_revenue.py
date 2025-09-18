import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('online_retail.db')

# SQL query for daily revenue, running total, and country
query = '''
SELECT 
    DATE(InvoiceDate) AS InvoiceDate,
    Country,
    SUM(Quantity * UnitPrice) AS daily_revenue,
    SUM(SUM(Quantity * UnitPrice)) OVER (PARTITION BY Country ORDER BY DATE(InvoiceDate)) AS running_total
FROM online_retail
GROUP BY Country, DATE(InvoiceDate)
ORDER BY Country, DATE(InvoiceDate);
'''

# Read the query result into a DataFrame
result_df = pd.read_sql_query(query, conn)

# Write the DataFrame to a CSV file
result_df.to_csv('daily_revenue_by_country.csv', index=False)

conn.close()
print("Exported daily revenue by country to daily_revenue_by_country.csv")
