from time import time

def timeit(func):
    def wrapper(*args, **kw):
        start = time()
        result = func(*args, **kw)
        duration = 1000 * (time() - start)
        print(f'\nit took {duration:.3f} ms.')
        return result
    return wrapper