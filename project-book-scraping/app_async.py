import asyncio
import aiohttp
import async_timeout
import requests
import time
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

loop = asyncio.get_event_loop()

books = page.books


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests tool {time.time() - start}')

for page_content in pages:
    logger.info('Creating BooksPage from page content.')

    books_page = BooksPage(page_content)
    books.extend(books_page.books)
