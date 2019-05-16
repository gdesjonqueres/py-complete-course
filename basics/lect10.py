my_name = 'Guillaume'
your_name = input('Enter your name: ')

print(f'{my_name} said: "hello {your_name}"')

age = input('Enter your age: ')
print(f'You have lived for {age * 12} months')

age = int(input('Enter your age: '))
print(f'You have lived for {age * 12} months')

age = int(input('Enter your age: '))
months = age * 12
seconds = age * 365 * 24 * 3600
print(f'You have lived for {months} months')
print(f'You have lived for {seconds} seconds')
