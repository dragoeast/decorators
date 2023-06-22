def timer_decorator(original_func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = original_func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"{original_func.__name__} run in {elapsed_time} sec.")
        return result
    
    return wrapper

import time

@timer_decorator
def display_info(name, age):
    time.sleep(3)
    print(f"{name}, {age}")

display_info('Krisztian', age=46)