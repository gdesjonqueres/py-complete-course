my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 16
}

for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago')

if 'Anne' in my_friends:
    print('I know Anne')

print(my_friends.items())
for t in my_friends.items():
    n, v = t
    print(f'I last saw {n} {v} days ago')
