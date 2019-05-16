top_friends = ['Jose', 'Rolf', 'Anna']

for i in range(3):
    print(f'my top {i+1} friend is: {top_friends[i]}.')

# instead of range, use enumerate when having to access item index:
for i, friend in enumerate(top_friends):
    print(f'my top {i+1} friend is {friend}.')

# enumerate gives a generator
# so it is possible to do:
friends_gen = enumerate(top_friends)
print(next(friends_gen))  # returns a tuple (index, item)
k, v = next(friends_gen)  # can do destructuring then
print(k)
print(v)
