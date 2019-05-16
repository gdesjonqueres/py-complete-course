for num in range(2, 20):
    if num % 2 == 0:
        print(f'Found an even number, {num}.')
        continue
    print(f'Found a number, {num}.')

# prime numbers
for n in range(2, 10): # [2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(2, n): # [], [2], [2, 3], [2, 3, 4]
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')
