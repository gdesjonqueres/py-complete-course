"""
Concerned with storing and retrieving books from a CSV file.
Format of the CSV file:

name,author,read\n
"""


books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'w'):
        pass  # just to make sure the file is here


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0')


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': bool(int(line[2]))}
        for line in lines
    ]


def mark_book_as_read_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
            break
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            read = int(book['read'])
            file.write(f"{book['name']},{book['author']},{read}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
