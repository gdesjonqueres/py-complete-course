def check_primes(limit):
    for n in range(2, limit + 1):
        check_if_prime(n)

## Check if prime number
def check_if_prime(n):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} is equal to {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')

check_primes(100)
