def decorator_function(original_function):

    def wrapper_function():
        return original_function()
    return wrapper_function

def display_function():
    print('display function runs')

decorated_display = decorator_function(display_function)

decorated_display()
