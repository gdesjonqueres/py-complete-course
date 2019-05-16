friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))
# this is equivalent to:
friends_lower = [f.lower() for f in friends]
friends_lower = (f.lower() for f in friends)  # prefer generator comprehension over the other two


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return self(data['name'], data['password'])

user_list = [
    {'name': 'Jose', 'password': '123'},
    {'name': 'Rolf', 'password': '456'}
]

users = [User.from_dict(user) for user in user_list]
# in this case map is preferable because it is more readable
# and there no overhead of declaring a variable 'user' as in the comprehension
users = map(User.from_dict, user_list)
