print((lambda x, y: x + y)(10, 5))

add = lambda x, y: x + y

# high order function: function that accepts a function as a argument
def who(some_data, identify):
    print(identify(some_data))

user = {'name' : 'jose', 'surname': 'salvatierra'}

who(user, lambda x: x['name'])
