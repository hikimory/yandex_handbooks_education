import sys

def check_continuity(function_str: str, x0: float, delta: float) -> None:
    K: int = 5
    epsilon: float = K * delta

    def f(x: float) -> float:
        return eval(function_str)

    f_x0: float = f(x0)
    left_limit: float = f(x0 - delta)
    right_limit: float = f(x0 + delta)
    
    if (abs(left_limit - f_x0) < epsilon) and (abs(right_limit - f_x0) < epsilon):
        print("CONTINUOUS")
    else:
        print("DISCONTINUOUS")

def main() -> None:
    function_str = input()
    x0 = float(input())
    delta = float(input())
    check_continuity(function_str, x0, delta)

if __name__ == '__main__':
    main()