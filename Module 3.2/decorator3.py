from functools import wraps
import random
import time


def cache(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key in wrapper.cache:
            output = wrapper.cache[cache_key]
        else:
            output = function(*args)
            wrapper.cache[cache_key] = output
        return output
    wrapper.cache = dict()
    return wrapper


@cache
def heavy_processing(n):
    sleep_time = n + random.random()
    time.sleep(sleep_time)


print(heavy_processing(3))