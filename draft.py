
from functions.create_db import create_db
from functions.drop_table import drop_table
drop_table(
    database= 'mydatabase'
    table_name = 'cliente'
)
create_db('mydatabase')

import sqlite3

def create_db(
    database_name: str
) -> sqlite3.Connection:
    """
    Create a new SQLite database or connect to an existing one.

    Args:
    database_name (str): The name of the database to create or connect to.

    Returns:
    sqlite3.Connection: A connection object to the SQLite database.
    """
    return sqlite3.connect(f'{database_name}.db')


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
cursor = conn.cursor()#faz com que consiga passar querys para dentro do banco
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente 
               (
               id_cliente INT,
               nome TEXT
               )          
               """)

cursor.execute
("""
    DROP TABLE cliente
""")

query = """
    SELECT name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""

pd.read_sql_query(query,conn)

