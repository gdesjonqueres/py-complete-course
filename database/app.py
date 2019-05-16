# from utils import database
# from utils import database_csv as database
# from utils import database_json as database
from utils import database_sql as database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' to save books
- 'lo' to load your books
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Please enter name: ')
    author = input('Please enter author: ')

    if not database.add_book(name, author):
        print('Book already in the library.')


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input('Please enter name: ')
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Please enter name: ')
    database.delete_book(name)


# def load_books():
#     database.load_json('books.json')
#
#
# def save_books():
#     database.save_to_json('books.json')


menu()
