import itertools
def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    previous = {}
    while len(visited) < len(graph):
        min_distance = float('inf')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex
        if min_vertex is None:
            break
        visited.add(min_vertex)
        for neighbor, weight in graph[min_vertex].items():
            new_distance = distances[min_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = min_vertex
    return distances, previous
def reconstruct_path(previous, start, end):
    path = [end]
    while path[-1] != start:
        if path[-1] not in previous:
            return None #Path not found
        path.append(previous[path[-1]])
    return path[::-1]
    
def solve():
    n, m, v, o1, o2, o3 = map(int, input().split())
    edges = []
    for _ in range(m):
        u, vi, c = map(int, input().split())
        edges.append((u, vi, c))
    graph = {i: {} for i in range(1, n + 1)}
    for u, vi, c in edges:
        graph[u][vi] = c
        graph[vi][u] = c
    orders = [o1, o2, o3]
    best_path = None
    min_distance = float('inf')
    for permutation in itertools.permutations(orders):
        current_path = [v]
        total_distance = 0
        last_node = v
        for order in permutation:
            distances, previous = dijkstra(graph, last_node)
            if order not in distances or distances[order] == float('inf'):
                total_distance = float('inf')
                break
            path_segment = reconstruct_path(previous, last_node, order)
            if path_segment is None:
                total_distance = float('inf')
                break
            current_path.extend(path_segment[1:])
            total_distance += distances[order]
            last_node = order
        distances, previous = dijkstra(graph, last_node)
        if v not in distances or distances[v] == float('inf'):
            total_distance = float('inf')
        else:
            path_segment = reconstruct_path(previous, last_node, v)
            if path_segment is None:
                total_distance = float('inf')
            else:
                current_path.extend(path_segment[1:])
                total_distance += distances[v]
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = current_path
    print(len(best_path))
    print(*best_path)

def main():
    solve()

if __name__ == "__main__":
    main()