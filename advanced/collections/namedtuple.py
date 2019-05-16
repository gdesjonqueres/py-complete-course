from collections import namedtuple

account = ('checking', 3547)
Account = namedtuple('Account', ['name', 'balance'])

accountNamedTuple = Account(*account)
accountNamedTuple = Account._make(account)  # from a tuple
print(accountNamedTuple._asdict()['balance']) # get a dictionnary
