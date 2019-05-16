# In Python we use processes when we have a multi-code machine and want to do calculations in parallel
# But using multi-process is complicated, specially considering sharing resources

import time
from multiprocessing import Process


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

process = Process(target=complex_calculation)
#process2 = Process(target=ask_user)  # we will have an error if we do that as the process
# don't have access to the terminal process2 will raise an EOF error
process2 = Process(target=complex_calculation)

start = time.time()

process.start()
process2.start()
# ask_user()

process.join()
process2.join()

print(f'total two process: {time.time() - start}')
