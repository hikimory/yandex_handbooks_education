import math
from typing import Callable
import numpy as np


def is_lipschitz(f: Callable[[float], float], a: float, b: float, L: float, num_points: int = 1000) -> bool:
    """
    Проверяет, является ли функция f(x) Липшицевой непрерывной на интервале [a, b] с константой L.

    Args:
        f: Функция f(x).
        a: Начало интервала.
        b: Конец интервала.
        L: Константа Липшица.
        num_points: Количество точек для дискретизации интервала.

    Returns:
        True, если функция Липшицева непрерывна с константой L, иначе False.
    """

    x_values = np.linspace(a, b, num_points)
    epsilon: float = 1e-6
    
    for i in range(num_points):
      for j in range(i + 1, num_points):
        x1 = x_values[i]
        x2 = x_values[j]
        if abs(f(x1) - f(x2)) > L * abs(x1 - x2) + epsilon:
            return False
    
    return True

def main() -> None:
    f_expr = input().strip()
    a, b = map(float, input().split())
    e = math.e
    L = eval(input().strip())
    fx = eval('lambda x, e=e: ' + f_expr)
    
    if is_lipschitz(fx, a, b, L):
       print("LIPSCHITZ")
    else:
        print("NOT LIPSCHITZ")

if __name__ == "__main__":
    main()