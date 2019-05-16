# Default arguments: never use a mutable as a Default value !
# def toto(titi = [])
# default value get initialized at the definition of the function
# not at every call making it keep its value over each call !

accounts = {
    'checking': 3000,
    'savings': 5000
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return
    the new balance."""
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.00, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

print(accounts)

for t in transactions:
    # unpacking tuple
    add_balance(*t)

    # named arguments
    add_balance(name=t[1], amount=t[0])

print(accounts)

# named arguments unpacking or dictionnary arguments unpacking

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # we don't need this anymore !
    @classmethod
    def from_dict(cls, data):
        return self(data['username'], data['password'])


user_list = [
    {'username': 'Jose', 'password': '123'},
    {'username': 'Rolf', 'password': '456'}
]

users = [User(username=data['username'], password=data['password']) for data in user_list]

# unpacking dictionnary does the exact same thing:
users = [User(**data) for data in user_list]
