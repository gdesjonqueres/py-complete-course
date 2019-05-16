def starts_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(starts_with_r, friends) # arg 1 function that truthy or falsy value
# or we can use a lambda function
start_with_r = filter(lambda friend: friend.startswith('R'), friends) # arg 1 function that returns True or False

# filter returns a generator !
# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

# can transform the generator to a list
print(list(start_with_r))
# list is empty because the generator has been exhausted already
print(list(start_with_r))

# the filter function returns the same generator as the following generator comprehension:
# generator comprehension is more effecient as we don't have to create a lamda function in this case
another_starts_with_r = (f for f in friends if f.startswith('R'))

# we could define it this way as well:
def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

start_with_r = my_custom_filter(lambda friend: friend.startswith('R'), friends)
