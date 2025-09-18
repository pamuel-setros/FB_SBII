import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
csv_file = 'Online_Retail.csv'
df = pd.read_csv(csv_file)

# Connect to SQLite database (it will be created if it doesn't exist)
db_file = 'online_retail.db'
conn = sqlite3.connect(db_file)

# Write the DataFrame to a table named 'online_retail'
df.to_sql('online_retail', conn, if_exists='replace', index=False)

conn.close()
print(f"Imported '{csv_file}' into '{db_file}' as table 'online_retail'.")
