from typing import Callable, Literal
from numpy import sin, cos, pi, tan, sqrt, log
from decorators import timeit
import numpy as np
import math


@timeit
def integral_midpoint_classic(f: Callable[[float], float], x0: float, x1: float, dx: float = .001) -> float:
    x, s = x0, 0
    while x < x1:
        s += f(x + dx/2)
        x += dx
    return s * dx


@timeit
def integral_midpoint(func: Callable[[np.ndarray], np.ndarray], x0: float, x1: float, dx: float = 1e-7) -> float:
    x = np.arange(x0 + dx/2, x1, dx)
    f = func(x)
    return np.sum(f) * dx


@timeit
def integral_simplson(func: Callable[[np.ndarray], np.ndarray], x0: float, x1: float, dx: float = 1e-7) -> float:
    n = math.floor((x1 - x0) / dx)
    n = n if n % 2 == 0 else n + 1
    dx = (x1 - x0) / n
    x = np.arange(x0, x1 + dx, dx)
    f = func(x)
    mult = np.arange(n + 1)
    mult = np.where(mult % 2 == 0, 2, 4)
    mult[0] = mult[n] = 1
    return np.sum(f * mult) * dx / 3


def integral(
        f: Callable[[np.ndarray], np.ndarray], 
        x0: float, x1: float, dx: float = 1e-7, 
        method: Literal['midpoint', 'simpson'] = 'simpson',
        use_np: bool = True) -> float:
    if method == 'simpson' and use_np:
        return integral_simplson(f, x0, x1, dx)
    elif method == 'midpoint' and use_np:
        return integral_midpoint(f, x0, x1, dx) 
    elif method == 'midpoint' and not use_np:
        return integral_midpoint_classic(f, x0, x1, dx)
    else: 
        raise Exception('Not impleneted')


if (__name__ == '__main__'):
    f = lambda x: sqrt(x**3 - 1)
    a = 1
    
    b = 2
    dx = .1
    print(integral(f, a, b, dx))
    quit()
    f = lambda x: cos(x)
    a = 0
    b = pi /2
    dx = .001
    print(integral(f, a, b, dx, 'midpoint', False))
    print(integral(f, a, b, dx, 'midpoint'))
    print(integral(f, a, b, dx))
