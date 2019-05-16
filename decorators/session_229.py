# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'adminable'
}

# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')

# ---- Do not change the code above ----


# You code starts here:
# Define a check_permission() decorator:
# a decorator is a higher order function, a function that takes a function as a parameter, wraps it and return it
def check_permission(func):
    if user['role'] == 'admin':
        return func
    raise PermissionError('You are not an admin.')

# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
secure_delete_database = check_permission(delete_database)

secure_delete_database()
