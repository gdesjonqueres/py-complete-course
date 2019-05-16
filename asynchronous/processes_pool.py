import time
from concurrent.futures import ProcessPoolExecutor


def ask_user():
    start = time.time()
    name = input('Please enter your name: ')
    print(f'Hello {name}.')
    print(f'ask_user: {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Starting complex calculation...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation: {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'total time single thread: {time.time() - start}')


# Processes

start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

print(f'total two process: {time.time() - start}')
