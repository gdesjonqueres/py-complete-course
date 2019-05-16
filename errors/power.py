def power_of_two():
    try:
        n = float(input('Value: '))
    except ValueError:
        print('Please enter a numeric value')
        return 0
    else:
        return n ** 2


def power_of_two2():
    # everything we want to try, put it in the try block
    # use finally for closing down something only
    try:
        n = float(input('Value: '))
        return n ** 2
    except ValueError:
        print('Please enter a numeric value')
        return 0


v = power_of_two2()
print(v)