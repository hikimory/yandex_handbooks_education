from collections import defaultdict
def create_graph(n, m):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for _ in range(m):
        u, v, t = map(int, input().split())
        if t == 1:
            graph[u].append(v)
            in_degree[v] += 1
        else:
            graph[v].append(u)
            in_degree[u] += 1
    return graph, in_degree

def can_determine_ranking(n, m):
    graph, in_degree = create_graph(n, m)
    
    stack = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            stack.append(i)

    count = 0
    while stack:
        if len(stack) > 1:
            return "NO"
        current = stack.pop()
        count += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    return "YES" if count == n else "NO"

def main():
    n, m = map(int, input().split())
    print(can_determine_ranking(n, m))
    
if __name__ == "__main__":
    main()