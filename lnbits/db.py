import sqlite3
import os
from .settings import DATABASE_PATH
from .settings import LNBITS_PATH


class Database:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def fetchall(self, query: str, values: tuple) -> list:
        """Given a query, return cursor.fetchall() rows."""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def fetchone(self, query: str, values: tuple):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def execute(self, query: str, values: tuple) -> None:
        """Given a query, cursor.execute() it."""
        self.cursor.execute(query, values)
        self.connection.commit()
        
       
class ExtDatabase:
    def __init__(self, db_path: str = os.path.join(LNBITS_PATH, "extensions", "overview.sqlite3")):
        self.path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def fetchall(self, query: str, values: tuple) -> list:
        """Given a query, return cursor.fetchall() rows."""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def fetchone(self, query: str, values: tuple):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def execute(self, query: str, values: tuple) -> None:
        """Given a query, cursor.execute() it."""
        self.cursor.execute(query, values)
        self.connection.commit()


class FauDatabase:
    def __init__(self, db_path: str = os.path.join(LNBITS_PATH, "extensions", "faucet", "database.sqlite3")):
        self.path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def fetchall(self, query: str, values: tuple) -> list:
        """Given a query, return cursor.fetchall() rows."""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def fetchone(self, query: str, values: tuple):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def execute(self, query: str, values: tuple) -> None:
        """Given a query, cursor.execute() it."""
        self.cursor.execute(query, values)
        self.connection.commit()

