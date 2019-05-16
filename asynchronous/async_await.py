from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g  # same as `yield from g`
    # await until the while loop in the coroutine ended
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, World! Multitasking...')
greeter.send('How are you?')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
