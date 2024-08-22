import sqlite3

def drop_table(database: str, table_name: str) -> None:
    """
    Creates a new table in the specified SQLite database.

    Args:
        database (str): The name of the database (without the '.db' extension).
        table_name (str): The name of the table to be created.

    Returns:
        None
    """
    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE {table_name}
        -- Add your table schema here
    """)

    conn.close()
