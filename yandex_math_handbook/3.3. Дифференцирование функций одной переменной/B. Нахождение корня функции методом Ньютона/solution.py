from typing import Tuple

def fx(x: float, coeffs: Tuple[float, float, float]) -> float:
    """Вычисляет значение функции в точке x."""
    a, b, c = coeffs
    return a * x**2 + b * x + c

def dfx(x: float, coeffs: Tuple[float, float, float]) -> float:
    """Вычисляет значение производной функции в точке x."""
    a, b, _  = coeffs
    return 2 * a * x + b

def newton_quadratic(coeffs: Tuple[float, float, float], x0: float, 
                     epsilon: float = 1e-6, max_iter: int = 1000) -> None:
    """
    Нахождение корня квадратного уравнения ax^2 + bx + c = 0 методом Ньютона.
    
    Args:
        coeffs: Коэффициенты (a, b, c).
        x0: Начальное приближение.
        epsilon: Погрешность.
        max_iter: Максимальное количество итераций.
    
    Returns:
        None
    """

    x: float = x0
    for i in range(1, max_iter + 1):
        fx_: float = fx(x, coeffs)
        dfx_: float = dfx(x, coeffs)
        
        if abs(dfx_) < 1e-10:
           if abs(fx_) < epsilon: # Проверяем, является ли x корнем
                print(f"Root found: x = {x:.6f}")
                print(f"Number of iterations: {0}")
                return
           else:   # производная 0, но x не является корнем
                print("Solution not found")
                return
        
        x_new: float = x - fx_ / dfx_
        
        if abs(fx(x_new, coeffs)) < epsilon:
            print(f"Root found: x = {x_new:.6f}")
            print(f"Number of iterations: {i}")
            return
        
        x = x_new
    
    # Превышено максимальное количество итераций, метод не сошелся
    print("Solution not found")
  
def main() -> None:
    coeffs_input = input().split()
    coeffs = tuple(map(float, coeffs_input))
    
    x0 = float(input())
    epsilon = float(input())

    newton_quadratic(coeffs, x0, epsilon)

if __name__ == "__main__":
    main()