# threads in Python help to reduce waiting time, because of the GIL,
# Python cannot really do multiple threading in paralel but do time slicing instead

import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    name = input('Please enter your name: ')
    print(f'Hello {name}.')
    print(f'ask_user: {time.time() - start}')


def complex_calculation():
    start = time.time()
    [x**2 for x in range(20000000)]
    print(f'complex_calculation: {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'total time single thread: {time.time() - start}')


start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
    # pool.shutdown() # blocking execution, wait for all threads to finish, like join()
    # we don't need to do it here as the context manager is doing it for us

print(f'total time two threads: {time.time() - start}')
