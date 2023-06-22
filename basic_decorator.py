def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print(f"wrapper function runs wigh {args} and {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_function(name, age):
    print(f'display function runs with name: {name} and age: {age}')


display_function('Krisztian', age=46)
