# def input_friend():
#     friend = yield
#     print(f'Hello {friend}')
#
# g = input_friend()
# g.send(None)  # priming the generator
# g.send('Robert')

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Anna'))


# we call this kind of generator "co-routine"
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)
    # we can do this as well with just the line: `yield from g`


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, World! Multitasking...')
greeter.send('How are you?')
