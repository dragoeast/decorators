# Decorator class instead of decorator function
class decorator_class:
    def __init__(self, original_function) -> None:
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f"__call__ function executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print(f"wrapper function executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_class
def display_function(name, age):
    print(f"display_function executed with {name} and {age}")

display_function('Kris', age=46)
