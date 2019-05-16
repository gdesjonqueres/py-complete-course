def countdown(n):
    while n  > 0:
        yield n
        n -= 1


c1 = countdown(10)
c2 = countdown(20)

# we can make this look like they are running at the same time
# by time slicing like python is doing with theads (no parallel in Python)
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))


# task scheduling, collaborative multi tasking without thread
tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)  # cheaper than switching to another thread
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')
