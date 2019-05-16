import functools

user = {'username': 'jose123', 'access_level': 'admin'}


# now the decorator is generic it accepts any arguments
def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            """
            Wraps func
            """
            if user.get('access_level') == access_level:
                return func(*args, **kwargs)
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel
    """
    return f'The password for {panel} panel is `TheToto!`.'


@user_has_permission('admin')
def another_function():
    pass


print(my_function('movies'))
print(another_function())
