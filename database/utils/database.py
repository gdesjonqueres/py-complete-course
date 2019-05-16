"""
Concerned with storing and retrieving books from a list.
"""

import json


books = []


def add_book(name, author):
    books.append({
        'name': name,
        'author': author,
        'read': False
    })


def get_all_books():
    return books


def mark_book_as_read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            return


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


# def delete_book(books, name):
#     found = -1
#     for i, book in enumerate(books):
#         if book['name'] == name:
#             found = i
#             break
#     if found >= 0:
#         del books[i:i+1]


# def delete_book(books, name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)  # bad practice to modify a list when iterating over it


def load_json(file_path):
    global books
    json_file = open(file_path, 'r')
    books = json.load(json_file)
    json_file.close()


def save_to_json(file_path):
    json_file = open(file_path, 'w')
    json.dump(books, json_file)
    json_file.close()
