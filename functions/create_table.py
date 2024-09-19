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