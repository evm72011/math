from typing import Callable
from autograd import grad, value_and_grad, numpy
from math import pi, sin, cos



def newton(
        f: Callable[[float], float],
        x0: float,
        df: Callable[[float], float] = None,
        delta: float = .001,
        max_iter: int = 100,
        silly = False) -> tuple[float, float]:
    df = grad(f) if df is None else df
    x = x0
    _f = f(x)
    for _ in range(max_iter):
        x = x - f(x) / df(x)
        _f = f(x)
        if abs(_f) < delta: 
            break
    assert abs(_f) < delta or silly
    return x, _f


if __name__ == "__main__":
    print(14*sin(2*0.536))
    f = lambda x: pi/3 - x - sin(x)
    df = lambda x: -1 - cos(x)
    print(newton(f, 0.5, df, 0.000001, 1000))
    quit()

    f = lambda x: x**2 - 4
    print(newton(f, 1.0))
    quit()

    f = lambda x: (4 * x**3 + 2 * x + 10) / 50
    print(newton(f, 1.0))

    f = lambda x: (4 * x**3 + 2 * x + 10) / 50
    df = lambda x: (12 * x**2 + 2) / 50
    print(newton(f, 1.0, df))