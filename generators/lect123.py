class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # allows us to do next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    # instead of having an iterable class our generator can also be an iterable by defining __iter__
    def __iter__(self):
        return self

print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)


# this is an iterable as well
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)

# iterators are used to get the next value.
# iterables are used to go over all the values of an iterator

# it is possible to do iterator comprehension as well as list comprehension
my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5]) # not a tuple, generator comprehension

print(my_numbers_gen)

print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
