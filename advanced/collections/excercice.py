from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    friends = defaultdict(lambda: 'Unknown')
    friends['Alan'] = 'Manchester'

    return friends


def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    # you code starts here:
    # remove the first entry
    arg_od.popitem(False)
    # remove the last entry
    arg_od.popitem()
    # move Bob to the end
    arg_od.move_to_end('Bob')
    # move Dan to the start
    arg_od.move_to_end('Dan', False)


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    Player = namedtuple('Player', ['name', 'club'])
    return Player(name, club)


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    # Remove first element
    arg_deque.pop()
    # move the first element to the end
    arg_deque.append(arg_deque.popleft())
    # add Zack to the start
    arg_deque.appendleft('Zack')

dd = task1()
print(dd['Alan'])
print(dd['JeanMi'])

od = OrderedDict({
    'Michel': 1,
    'Paul': 2,
    'Bob': 3,
    'Dan': 4,
    'Raymond': 5
})
task2(od)
print(od)

nt = task3('JeanPaul', 'FC Girondins de Bordeaux')
print(nt)

dq = deque(('JeanMi', 'JeanPaul', 'JeanPierre'))
task4(dq)
print(dq)
