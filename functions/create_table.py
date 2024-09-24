import sqlite3

def create_table(
    database:str,
    table_name:str,
    columns_desc:str
) -> None:
    """
    Creates a table in the specified SQLite database.

    Args:
        database (str): The name of the database (without the .db extension).
        table_name (str): The name of the table to be created.
        columns_desc (str): A string describing the columns of the table, including column names, data types, and constraints (e.g., "id INTEGER PRIMARY KEY, name TEXT NOT NULL").

    Returns:
        None: This function does not return any value.
    """

    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
   f"""
    CREATE TABLE IF NOT EXISTS {table_name}
       ({columns_desc}) 
    """
)

    conn.close()

create_table(
    database='mydatabase',
    table_name='Cliente',
    columns_desc="""
       ID_Cliente INTEGER PRIMARY KEY NOT NULL,
       Nome VARCHAR(20) NOT NULL,
       Sobrenome VARCHAR(20),
       Genero CHAR(10),
       CPF CHAR(11),
       Celular CHAR(15) NOT NULL,
       E_mail CHAR(20)
    """
)

create_table(
    database='mydatabase',
    table_name='Endereço',
    columns_desc="""
       ID_Endereço INTEGER PRIMARY KEY NOT NULL,
       CEP CHAR(8),
       Logradouro CHAR(30),
       N_Da_Casa CHAR(10),
       Complemento CHAR(30),
       Bairro CHAR(20),
       Cidade CHAR(20),
       Estado CHAR(15),
       ID_Cliente INTEGER,
       FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
    """
)

create_table(
    database='mydatabase',
    table_name='Carrinho',
    columns_desc="""
       ID_Carrinho INTEGER PRIMARY KEY NOT NULL,
       Horario CHAR(4) NOT NULL,
       Data CHAR(9) NOT NULL,
       Quantidade_Produtos CHAR(100) NOT NULL,
       Valor_Final FLOAT NOT NULL,
       Forma_pagamento CHAR(20) NOT NULL
    """
)

import sqlite3

def create_table(
    database:str,
    table_name:str,
    columns_desc:str
) -> None:
    """
    Creates a table in the specified SQLite database.

    Args:
        database (str): The name of the database (without the .db extension).
        table_name (str): The name of the table to be created.
        columns_desc (str): A string describing the columns of the table, including column names, data types, and constraints (e.g., "id INTEGER PRIMARY KEY, name TEXT NOT NULL").

    Returns:
        None: This function does not return any value.
    """

    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
   f"""
    CREATE TABLE IF NOT EXISTS {table_name}
       ({columns_desc}) 
    """
)

    conn.close()

create_table(
    database='mydatabase',
    table_name='Cliente',
    columns_desc="""
       ID_Cliente INTEGER PRIMARY KEY NOT NULL,
       Nome VARCHAR(20) NOT NULL,
       Sobrenome VARCHAR(20),
       Genero CHAR(10),
       CPF CHAR(11),
       Celular CHAR(15) NOT NULL,
       E_mail CHAR(20)
    """
)

create_table(
    database='mydatabase',
    table_name='Endereço',
    columns_desc="""
       ID_Endereço INTEGER PRIMARY KEY NOT NULL,
       CEP CHAR(8),
       Logradouro CHAR(30),
       N_Da_Casa CHAR(10),
       Complemento CHAR(30),
       Bairro CHAR(20),
       Cidade CHAR(20),
       Estado CHAR(15),
       ID_Cliente INTEGER,
       FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
    """
)

create_table(
    database='mydatabase',
    table_name='Carrinho',
    columns_desc="""
       ID_Carrinho INTEGER PRIMARY KEY NOT NULL,
       Horario CHAR(4) NOT NULL,
       Data CHAR(9) NOT NULL,
       Quantidade_Produtos CHAR(100) NOT NULL,
       Valor_Final FLOAT NOT NULL,
       Forma_pagamento CHAR(20) NOT NULL
    """
)

create_table(
    database='mydatabase',
    table_name='Produto',
    columns_desc="""
       ID_Produto INTEGER PRIMARY KEY NOT NULL,
       Item CHAR(6) NOT NULL,
       Preço_Um FLOAT NOT NULL,
       Quantidade_Estoque INTEGER NOT NULL,
       Tipo CHAR(15),
       Método_de_Venda CHAR(2)
    """
)

create_table(
    database='mydatabase',
    table_name='Compra',
    columns_desc="""
    ID_Compra INTEGER PRIMARY KEY NOT NULL,
    ID_Cliente INTEGER,
    ID_Produto INTEGER,
    ID_Carrinho INTEGER,
    Horario TIMESTAMP,
    Data DATE,
    Quantidade INTEGER,
    Valor DOUBLE,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (ID_Produto) REFERENCES Produto(ID_Produto),
    FOREIGN KEY (ID_Carrinho) REFERENCES Carrinho(ID_Carrinho)
    """
);



