# How to handle parameters with decorators ?
import functools

user = {'username': 'jose123', 'access_level': 'admin'}


# def third_level(access_level):
#     def user_has_permission(func):
#         @functools.wraps(func)
#         def secure_func(panel):
#             """
#             Wraps func
#             """
#             if user.get('access_level') == access_level:
#                 return func(panel)
#         return secure_func
#     return user_has_permission
#
#
# # using built-in decorator feature
# @third_level('admin')
# def my_function(panel):
#     """
#     Allows us to retrieve the password for the admin panel
#     """
#     return f'The password for {panel} panel is `TheToto!`.'


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            """
            Wraps func
            """
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel
    """
    return f'The password for {panel} panel is `TheToto!`.'


print(my_function('movies'))
