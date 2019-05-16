# threads in Python help to reduce waiting time, because of the GIL,
# Python cannot really do multiple threading in paralel but do time slicing instead

import time
from threading import Thread


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


thread1 = Thread(target=ask_user)
thread2 = Thread(target=complex_calculation)

start = time.time()

thread1.start()
thread2.start()

# don't kill a thread manually as it won't release the GIL
# then we will have a deadlock
# wait for it to finish

thread1.join()
thread2.join()

print(f'total time two threads: {time.time() - start}')
