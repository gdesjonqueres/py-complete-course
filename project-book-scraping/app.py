import requests
import logging

from pages.books_page import BooksPage


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename='logs.txt'
)
logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = BooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    page_url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    logger.info(f'Scraping books page no#{page_num+1}')
    page_content = requests.get(page_url).content

    books_page = BooksPage(page_content)
    books.extend(books_page.books)
