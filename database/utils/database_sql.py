import sqlite3
from typing import List, Dict, Union

from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.
"""


Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name: str, author: str) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        try:
            # cursor.execute(f'INSERT INTO books VALUES ("{name}", "{author}", 0)')  # insecure: open to SQL Injection
            cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
        except sqlite3.IntegrityError:
            return False
        # else:
        #     connection.commit()
        # finally:
        #     connection.close()

    return True


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        # books = cursor.fetchall()  # [(name, author, read), (name, author, read), ...]
        books = [{'name': row[0], 'author': row[1], 'read': bool(row[2])} for row in cursor.fetchall()]

    return books


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))  # comma to make sure it's a tuple


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name = ?', (name,))
