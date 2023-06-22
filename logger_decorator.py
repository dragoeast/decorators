def logger_decorator(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}.log", level=logging.INFO)


    def wrapper(*args, **kwargs):
        logging.info(msg=f"Run with args: {args} and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    
    return wrapper

@logger_decorator
def display_info(name, age):
    print(f"display_info run with arguments: {name}, {age}")

display_info('Krisztian', age=46)
