from typing import Tuple, List

def polynomial(x: float, coeffs: Tuple[float, float, float, float]) -> float:
    """Вычисляет значение полинома в точке x."""
    a, b, c, d = coeffs
    return a * x**3 + b * x**2 + c * x + d

def derivative(x: float, coeffs: Tuple[float, float, float, float]) -> float:
    """Вычисляет значение производной полинома в точке x."""
    a, b, c, _ = coeffs
    return 3 * a * x**2 + 2 * b * x + c

def second_derivative(x: float, coeffs: Tuple[float, float, float, float]) -> float:
    """Вычисляет значение второй производной полинома в точке x."""
    a, b, _, _ = coeffs
    return 6 * a * x + 2 * b
    
def get_point_type(x: float) -> str:
    """Определяет тип критической точки x со значением val"""
    if x > 0:
        return "Local minimum"
    elif x < 0:
        return "Local maximum"
    else:
        return "Saddle point"

def find_critical_points(coeffs: Tuple[float, float, float, float], p: float, q: float) -> List[Tuple[float, str, float]]:
    """Находит критические точки полинома на интервале [p, q] и определяет их характер."""
    a,b,c,_ = coeffs
    # Решение квадратного уравнения для нахождения корней производной
    # ax^2 + bx + c = 0
    # x = -b +/- sqrt(b^2 - 4ac) / 2a
    critical_points: List[float] = []

    if a == 0:
        if b > 0:
            point: float = 0.00000
            val: float = second_derivative(point, coeffs)
            point_type: str = get_point_type(val)
            critical_points.append((point, point_type, polynomial(point, coeffs)))
    else:
        critical_points: List[float] = []
        discriminant: float = (2*b)**2 - 4 * (3*a) * c
                
        if discriminant > 0:
            x1: float = (-2*b + discriminant**0.5) / (2 * 3*a)
            x2: float = (-2*b - discriminant**0.5) / (2 * 3*a)
            
            points: List[float] = sorted([x1, x2])
            
            for point in points:
                if p <= point <= q:
                    val: float = second_derivative(point, coeffs)
                    point_type: str = get_point_type(val)
                    critical_points.append((point, point_type, polynomial(point, coeffs)))
                    
        elif discriminant == 0:
            point: float = -2*b / (2 * 3*a)
            if p <= point <= q:
                val: float = second_derivative(point, coeffs)
                point_type: str = get_point_type(val)
                critical_points.append((point, point_type, polynomial(point, coeffs)))
    
    return critical_points

def main() -> None:
    coeffs_input = input().split()
    coeffs = tuple(map(float, coeffs_input))
    
    interval_input = input().split()
    p, q = map(float, interval_input)

    critical_points = find_critical_points(coeffs, p, q)

    if not critical_points:
        print("No critical points found.")
    else:
        for x, point_type, fx in critical_points:
            print(f"{point_type} at x = {x:.5f}")
            print(f"f(x) = {fx:.5f}")

if __name__ == "__main__":
    main()