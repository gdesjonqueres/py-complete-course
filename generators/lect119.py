def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1

g = hundred_numbers()
print(next(g))
print(next(g))

print(list(g))  # transform generator to a list starting from 2, the generator doesn't reset

my_range_object = range(10)
# next(my_range_object)  # it's not a generator but pretty ;uch the same

def prime_generator(bound):
    # your code starts here (delete the pass):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n

prime_numbers = prime_generator(100)
for n in prime_numbers:
    print(f'{n} is a prime number')
