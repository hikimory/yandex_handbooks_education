from typing import List

def adjacency_list_to_matrix(adj_list: List[List[int]], n: int) -> List[List[int]]:
    adj_matrix: List[List[int]] = [[0] * n for _ in range(n)]

    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = 1
    return adj_matrix


def main() -> None:
    n: int = int(input())
    adjacency_list: List[List[int]] = []
    for _ in range(n):
        neighbors: List[int] = list(map(int, input().split()))
        adjacency_list.append(neighbors)

    adjacency_matrix: List[List[int]] = adjacency_list_to_matrix(adjacency_list, n)

    for row in adjacency_matrix:
        print(*row)

if __name__ == "__main__":
    main()