names_list = ['John', 'Rolf', 'Anne']
lowercase_names = [s.lower() for s in names_list]
# print(lowercase_names)

friend = input('Enter your friend name: ')
print(friend.lower() in lowercase_names)

## With conditional
evens = list(range(10))[0::2]
print(evens)

evens = [n for n in range(10) if n % 2 == 0]
print(evens)

friends = ['rolf', 'anna', 'ruth', 'charlie']
guests = ['Jose', 'Rolf', 'Ruth', 'Charlie', 'michael']
# present_friends = [
#     friend for friend in friends if friend.lower() in [
#         guest.lower() for guest in guests
#     ]
# ]
# present_friends = [name.capitalize() for name in guests if name.lower() in friends]
lowercase_friends = [name.lower() for name in friends]
present_friends = [name.capitalize() for name in guests if name.lower() in lowercase_friends]
print(present_friends)

friends = {'rolf', 'anna', 'charlie'}
guests = {'jose', 'rolf', 'ruth', 'charlie', 'michael'}
present_friends = {name.capitalize() for name in guests & friends}
print(present_friends)

names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]
friends_last_seen = {
    names[i]: time_last_seen[i] for i in range(len(names))
}
print (friends_last_seen)

friends_last_seen = dict(zip(names, time_last_seen))
print (friends_last_seen)
