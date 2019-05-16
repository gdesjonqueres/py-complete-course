import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.title}, rated: {self.rating}, price: {self.price}>'

    @property
    def title(self):
        logger.debug('Finding book title...')
        title_tag = self.parent.select_one(BookLocators.TITLE)
        title = title_tag.attrs[BookLocators.TITLE_ATTR]
        logger.debug(f'Found book title, `{title}`')
        return title

    @property
    def link(self):
        logger.debug('Finding book link...')
        link_tag = self.parent.select_one(BookLocators.LINK)
        link = link_tag.attrs['href']
        logger.debug(f'Found book link, `{link}`.')
        return link

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        rating_tag = self.parent.select_one(BookLocators.RATING)
        rating_classes = rating_tag.attrs['class']
        rating_classes = [c for c in rating_classes if c != BookLocators.RATING_EXCLUDE]
        rating_number = int(BookParser.RATINGS.get(rating_classes[0]))
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number

    @property
    def price(self):
        logger.debug('Finding book price...')
        price_tag = self.parent.select_one(BookLocators.PRICE)
        matcher = re.search(BookLocators.PRICE_REGEX, price_tag.string)
        price = float(matcher.group(1))
        logger.debug(f'Found book price, `{price}`.')
        return price
