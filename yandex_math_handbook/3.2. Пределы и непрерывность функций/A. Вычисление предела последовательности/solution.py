import sys

def main() -> None:
    N: int = int(input())
    an: float = N / (N + 1)
    print(f"{an:.6f}")

if __name__ == '__main__':
    main()