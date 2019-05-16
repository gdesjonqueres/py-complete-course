import logging

from app import books


logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 't' to display the total number of books in catalogue
- 'q' to exit

Enter your choice: '''


def print_best():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda b: (b.rating * -1, b.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda b: b.price)[:10]
    for book in cheapest_books:
        print(book)


def print_five_stars_books():
    logger.info('Finding 5 star rating books...')
    five_stars_books = [b for b in books if b.rating == 5][:10]
    for book in five_stars_books:
        print(book)


# def get_next_book():
#     for book in books:
#         yield book
#
#
# next_book = get_next_book()
books_generator = (x for x in books)  # creates a generator


def print_next_book():
    logger.info('Finding next book...')
    # print(next(next_book))
    print(next(books_generator))


def print_total_no_items():
    logger.info('Finding number of books in collection...')
    print(len(books))


user_choices = {
    'b': print_five_stars_books,
    'c': print_cheapest,
    'n': print_next_book,
    't': print_total_no_items
}


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in user_choices.keys():
            user_choices[user_input]()
        else:
            print('Please type a valid command.')

        user_input = input(USER_CHOICE)

    logger.info('Terminating application...')


menu()
