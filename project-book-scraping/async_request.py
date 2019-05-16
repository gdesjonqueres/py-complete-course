import aiohttp
import asyncio
import time


# return a coroutine object
async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:  # creates a connexion pool
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status


loop = asyncio.get_event_loop()
tasks = [fetch_page('http://google.com') for _ in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start}')
