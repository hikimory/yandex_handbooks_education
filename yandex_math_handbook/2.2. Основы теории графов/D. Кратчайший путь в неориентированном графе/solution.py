from collections import deque
from typing import List, Tuple, Set


def bfs(graph: List[List[int]], start: int, target: int) -> int:
    n: int = len(graph)
    queue: deque[Tuple[int, int]] = deque([(start, 0)])  # (vertex, distance)
    visited: Set[int] = {start}

    while queue:
        current_node, distance = queue.popleft()

        if current_node == target:
            return distance

        for neighbor in range(n):
            if graph[current_node][neighbor] == 1 and neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)
    return -1

def main() -> None:
    n: int = int(input())
    adjacency_matrix: List[List[int]] = []
    for _ in range(n):
        row: List[int] = list(map(int, input().split()))
        adjacency_matrix.append(row)

    start_node, target_node = map(int, input().split())
    shortest_path_length: int = bfs(adjacency_matrix, start_node, target_node)
    print(shortest_path_length)

if __name__ == "__main__":
    main()