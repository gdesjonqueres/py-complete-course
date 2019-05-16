# class RuntimeErrorWithCode(TypeError):
class RuntimeErrorWithCode(Exception):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code


# raise RuntimeErrorWithCode('An error happened.', 500)

err = RuntimeErrorWithCode('An error happened.', 500)
print(err.__doc__)