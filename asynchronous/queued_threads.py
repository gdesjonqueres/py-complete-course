import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()  # things to be printed out
counter_queue = queue.Queue()  # amounts by which to increase the counter


def increment_manager():
    global counter
    while True:
        # creates a bottle neck to access the state
        increment = counter_queue.get()  # this waits until an item is available and then locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New counter value is {counter}', '--------'))
        time.sleep(random.random())
        counter_queue.task_done()  # this unlocks the queue


# daemon=True => runs continuously
Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    time.sleep(random.random())
    counter_queue.put(1)


# we could use a ThreadPoolExecutor here instead to make things a bit more simple
worker_threads = [Thread(target=increment_counter) for _ in range(10)]

for thread in worker_threads:
    thread.start()


for thread in worker_threads:
    thread.join()


# joigning the queues not the daemon
counter_queue.join()
job_queue.join()
