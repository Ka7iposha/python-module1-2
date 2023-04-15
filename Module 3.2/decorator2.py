import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("%.6f" % (end - start))
        return result
    return wrapper


@timeit
def process_data(a, b):
    return a + b


process_data(1, 3)
