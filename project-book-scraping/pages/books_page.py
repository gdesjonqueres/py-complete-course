import re
import logging
from bs4 import BeautifulSoup

from locators.books_page import BooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, html_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(html_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BooksPageLocators.BOOK}`.')
        locator = BooksPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(b) for b in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding number of catalogue pages available...')
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages
