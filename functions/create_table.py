import sqlite3

def create_table(database, table_name, columns_desc):
    """
    Cria uma tabela no banco de dados SQLite.

    Parameters
    ----------
    database : str
        O nome do banco de dados.
    table_name : str
        O nome da tabela a ser criada.
    columns_desc : str
        Uma string descrevendo as colunas e seus tipos (e.g., 'id INTEGER PRIMARY KEY, name TEXT').

    Returns
    -------
    None
        Esta função não retorna nenhum valor. Ela cria a tabela se ela não existir.
    """
    
    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns_desc})""")

    conn.close()
