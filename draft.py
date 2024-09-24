import pandas as pd
import sqlite3
from functions.create_table import create_table

create_table(
    database='mydatabase',
    table_name='Cliente',
    columns_desc="""
       ID_cliente INTEGER PRIMARY KEY NOT NULL,
       Nome VARCHAR(20) NOT NULL,
       Sobrenome VARCHAR(20),
       Genero CHAR(10),
       CPF CHAR(11),
       Celular CHAR(15) NOT NULL,
       E_mail CHAR(20),
       CEP CHAR(8),
       Logradouro CHAR(30),
       N_Da_Casa CHAR(10),
       Complemento CHAR(30),
       Bairro CHAR(20),
       Cidade CHAR(20),
       Estado CHAR(15)
    """
)


# create a data example
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create a connection
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame to a table in the database
data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

# closing the connection
conn.close()


########## 
conn = sqlite3.connect('mydatabase.db')

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""


pd.read_sql_query(query, conn)