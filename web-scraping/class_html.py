import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
        <div class="image_container">
            <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
        </div>
        <p class="star-rating Three">
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
        </p>
        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
        <div class="product_price">
            <p class="price_color">£51.77</p>
            <p class="instock availability">
                <i class="icon-ok"></i>
                In stock
            </p>
            <form>
                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
            </form>
        </div>
    </article>
</li>
</body></html>
'''


class ParsedItemLocator:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = '.product_price .price_color'
    RATING_LOCATOR = '.product_pod .star-rating'


class ParsedItem:
    def __init__(self, item_html):
        self.soup = BeautifulSoup(item_html, 'html.parser')

    def item_name(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    def item_link(self):
        locator = ParsedItemLocator.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    def item_price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        # item_price = float(item_price[1:])

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        print(matcher.group(0))
        return float(matcher.group(1))

    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        rating_tag = self.soup.select_one(locator)
        rating = [c for c in rating_tag.attrs.get('class') if c != 'star-rating']
        return rating[0]


parsed_item = ParsedItem(ITEM_HTML)
print(parsed_item.item_name())
print(parsed_item.item_link())
print(parsed_item.item_price())
print(parsed_item.rating())
