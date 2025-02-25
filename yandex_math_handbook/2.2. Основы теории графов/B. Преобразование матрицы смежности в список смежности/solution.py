import sys
from typing import List, Optional

def read_adjacency_matrix_from_file(filename: str = "input.txt") -> Optional[List[List[int]]]:
    try:
        with open(filename, "r") as f:
            adjacency_matrix: List[List[int]] = []
            for line in f:
                row: List[int] = list(map(int, line.strip().split()))
                adjacency_matrix.append(row)
            return adjacency_matrix

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError:
        print(f"Error: Invalid format in file '{filename}'. Ensure the file contains numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def adjacency_matrix_to_list(adjacency_matrix: List[List[int]]) -> None:
    if not adjacency_matrix:
        print("NO LOOPS")
        return
    
    n: int = len(adjacency_matrix)
    for i in range(n):
        neighbors: List[int] = []
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                neighbors.append(j)
        if neighbors:
            print(*neighbors)
        else:
            print()

def main() -> None:
    adjacency_matrix = read_adjacency_matrix_from_file()
    adjacency_matrix_to_list(adjacency_matrix)

if __name__ == '__main__':
    main()