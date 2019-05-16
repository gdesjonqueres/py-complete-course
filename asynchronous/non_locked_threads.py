import time
import random

from threading import Thread

counter = 0


def increment_counter():
    global counter
    # we are fuzzying (random sleep) to see how threads execute and if there is a problem
    # without this the function would execute very fast and each thread
    # will be finished as soon as another starts, executing almost sequentially
    # by doing this we can see that the counter is getting messed and the value
    # is not incrementing properly this is because multiple threads access the counter at once
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('--------------')


for _ in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
