import pandas as pd
import sqlite3
data= pd.DataFrame({
    'ID':[1,2,3,4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

conn=sqlite3.connect('mydatabase.db')

data.to_sql(
    'client', conn,
    if_exists = 'replace',
    index=False
)

conn.close()

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
query = """
    SELECT name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""

pd.read_sql_query(query,conn)

