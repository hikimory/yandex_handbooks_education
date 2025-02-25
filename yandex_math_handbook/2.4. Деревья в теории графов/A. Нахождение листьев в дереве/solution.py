import sys
from typing import List

def main() -> None:
    n: int = int(input())
    leaves: List[int] = []
    for i in range(n):
        if sum(list(map(int, input().split()))) == 1:
            leaves.append(i)
    if not leaves:
        print("NO LEAVES")
    else:
        print(*leaves, sep='\n')

if __name__ == '__main__':
    main()