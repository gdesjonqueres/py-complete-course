# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.number = 2

    # def __next__(self):
    #     print('********', self.number)
    #     if self.number < self.stop:
    #         for n in range(self.number, self.stop):
    #             for x in range(2, n):
    #                 if n % x == 0:
    #                     print('----', n)
    #                     self.number = n + 1
    #                     break
    #             else:
    #                 self.number = n + 1
    #                 return n
    #     else:
    #         raise StopIteration()

    def __next__(self):
        if self.number and self.number < self.stop:
            current = self.number
            self.number = self.get_next_prime(self.number + 1)
            return current
        else:
            raise StopIteration()

    def get_next_prime(self, start):
        next_prime = None
        for n in range(start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                next_prime = n
                break
        return next_prime


class PrimeGeneratorSolution:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator


# g = PrimeGenerator(12)
g = PrimeGeneratorSolution(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
