def is_bipartite(adj_matrix):
    """Проверяет, является ли граф двудольным.

    Args:
        adj_matrix: Матрица смежности вершин.

    Returns:
        bool: True, если граф двудольный, False - иначе.
    """

    n = len(adj_matrix)
    colors = [-1] * n

    def dfs(node, color):
        colors[node] = color
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == color:
                    return False
        return True

    for i in range(n):
        if colors[i] == -1:
            if not dfs(i, 0):
                return "NO"
    return "YES"

adj_matrix = [[0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]]

result = is_bipartite(adj_matrix)
print(result)