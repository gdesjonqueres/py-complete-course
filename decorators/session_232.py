import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        """
        Wraps func
        """
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


# using built-in decorator feature
@user_has_permission
def my_function():
    """
    Allows us to retrieve the password for the admin panel
    """
    return 'The password for the boss is TheToto!'


@user_has_permission
def another_function():
    pass


print(my_function())

# because the wrapper is decrorated using functool we can now get the real infos
print(my_function.__name__)
print(another_function.__name__)
print(my_function.__doc__)

# but how to handle parameters ? if we want to keep our decorator generic
