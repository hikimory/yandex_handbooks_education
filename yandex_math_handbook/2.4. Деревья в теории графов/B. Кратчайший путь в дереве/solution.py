import sys
from collections import deque
from typing import List, Tuple

def main() -> None:
    n: int = int(input())
    adj_matrix: List[List[int]] = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))

    r, v = map(int, input().split())

    adj_list: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)

    queue: deque[Tuple[int, List[int]]] = deque([(r, [r])])
    visited: List[bool] = [False] * n

    while queue:
        curr, path = queue.popleft()
        
        if curr == v:
          print(*path)
          return

        visited[curr] = True

        for neighbor in adj_list[curr]:
            if not visited[neighbor]:
                queue.append((neighbor, path + [neighbor]))
    
    print("NO PATH")

if __name__ == '__main__':
    main()