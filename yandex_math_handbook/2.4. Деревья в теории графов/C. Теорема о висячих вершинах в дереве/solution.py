import sys
from typing import List, Dict

def main() -> None:
    n: int = int(input())
    vertices: List[str] = input().split()
    m: int = int(input())

    if m == n - 1:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()