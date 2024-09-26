import pandas as pd
import sqlite3
from functions.create_table import create_table

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
       Metodo_de_Venda CHAR(2)
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

import sqlite3
from functions.inserts_rows import insert_one_row

# Dados a serem inseridos na tabela Cliente
rows = [
    ('140324202201', 'Thamires', 'Fernandes', 'Feminino', '100010010-01', '81987182384', 'thamires_a_gatinha@hotmail.com'),
    ('140324202427', 'Nathália', 'de Lima', 'Feminino', '111011110-01', '81985932755', 'tadsblocofeoefe@gmail.com'),
    ('140324210126', 'David', 'Esdras', 'Masculino', '568496115-45', '81987453695', 'edrasesaedras@gmail.com'),
    ('140324210128', 'Ana', 'Letícia', 'Feminino', '175986432-15', '81987572256', 'analetads@gmail.com')
]

# Inserir cada linha
for row in rows:
    values = ', '.join([f"'{value}'" for value in row])
    insert_one_row('mydatabase', 'Cliente', 'ID_Cliente, Nome, Sobrenome, Genero, CPF, Celular, E_mail', values)

# Dados a serem inseridos na tabela Endereço
rows_endereco = [
    (1, '140324202201', '50700270', 'Rua Estevão de Sá', '678', 'apto 104', 'CDU', 'Recife', 'Pernambuco'),
    (2, '140324202427', '55125789', 'Rua TADS', '1011001', 'bloco F', 'binarzea', 'TadsLandia', 'Mundo virtual'),
    (3, '140324210126', '55896487', 'Rua 20232IAI', '666', 'bloco A', 'binarzea', 'TadsLandia', 'Mundo virtual'),
    (4, '140324210128', '55126349', 'Rua 20232Vt', '333', 'bloco b', 'binarzea', 'TadsLandia', 'Mundo virtual')
]

# Inserir cada linha
for row in rows_endereco:
    values = ', '.join([f"'{value}'" for value in row])
    insert_one_row('mydatabase', 'Endereço', 'ID_Endereço, ID_Cliente, CEP, Logradouro, N_Da_Casa, Complemento, Bairro, Cidade, Estado', values)

# Dados a serem inseridos na tabela Carrinho
rows_carrinho = [
    (1, '15:45', '10/03/2024', 3, 'R$ 98,40', 'pix'),
    (2, '16:48', '14/03/2024', 2, 'R$ 32,00', 'credito'),
    (3, '17:50', '21/03/2024', 2, 'R$ 50,00', 'débito'),
    (4, '18:10', '22/03/2024', 5, 'R$ 80,00', 'pix')
]

# Inserir cada linha
for row in rows_carrinho:
    values = ', '.join([f"'{value}'" for value in row])
    insert_one_row('mydatabase', 'Carrinho', 'ID_Carrinho, Horario, Data, Quantidade_Produtos, Valor_Final, Forma_Pagamento', values)

# Dados a serem inseridos na tabela Produto
rows_produto = [
    (1, 'girassol', 'R$ 14,90', 30, 'planta', 'un'),
    (2, 'argila expandida', 'R$ 5,90', 12, 'substrato', 'kg'),
    (3, 'humus de minho', 'R$ 2,00', 10, 'fertilizante', 'kg'),
    (4, 'inseticida', 'R$ 20,00', 7, 'defensivo', 'un'),
    (5, 'planta suculenta', 'R$ 9,00', 12, 'planta', 'un')
]

# Inserir cada linha
for row in rows_produto:
    values = ', '.join([f"'{value}'" for value in row])
    insert_one_row('mydatabase', 'Produto', 'ID_Produto, Item, Preço_Um, Quantidade_Estoque, Tipo, Metodo_De_Venda', values)


# Dados a serem inseridos na tabela Compra
rows_compra = [
    (1, '140324202201', 1, 1, '15:45', '10/03/2024', 5, ' 74,50'),
    (2, '140324202201', 5, 1, '15:45', '10/03/2024', 2, ' 18,00'),
    (3, '140324202201', 2, 1, '15:46', '10/03/2024', 1, ' 5,90'),
    (4, '140324210126', 3, 2, '16:48', '10/03/2024', 6, ' 12,00')
]

# Inserir cada linha
for row in rows_compra:
    values = ', '.join([f"'{value}'" for value in row])
    insert_one_row('mydatabase', 'Compra', 'ID_Compra, ID_Cliente, ID_Produto, ID_Carrinho, Horario, Data, Quantidade, Valor', values)



