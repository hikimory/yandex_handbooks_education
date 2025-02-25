from collections import defaultdict

def is_bipartite(graph):
    """Проверяет, является ли граф двудольным.

    Args:
        graph: Словарь, представляющий граф. Ключи - вершины, значения - списки смежных вершин.

    Returns:
        bool: True, если граф двудольный, False - иначе.
    """

    colors = {}
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not dfs(neighbor, 3 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True

    for node in graph:
        if node not in colors:
            if not dfs(node, 1):
                return False
    return True

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

if is_bipartite(graph):
    print("YES")
else:
    print("NO")