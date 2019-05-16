friends = [
    {
        'name': 'Jose',
        'location': 'San Francisco'
    },
    {
        'name': 'Rolf',
        'location': 'San Francisco'
    },
    {
        'name': 'Maria',
        'location': 'San Francisco'
    },
    {
        'name': 'John',
        'location': 'Miami'
    }
]

location = input('Please state your location: ')
friends_nearby = [f for f in friends if f['location'] == location]

# any returns True if any item in the iterable is truthy
if any(friends_nearby):
    print('You are not alone !')
else:
    print('Make friends !')

# all returns False if all item are truthy
print(all([1, 2, 3, 4, 5]))
print(all([0, 1, 2, 3, 4, 5]))

"""
Evaluates to False:
* 0, 0.0
* None
* ''
* [], {}, ()
"""

bool(0)
