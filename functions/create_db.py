
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