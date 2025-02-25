from collections import deque

def find_shortest_path(n, m, maze):
    directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]

    start = end = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)

    if not start or not end:
        return -1

    queue = deque([start])
    visited = set()
    visited.add(start)
    
    parent = {}
    
    while queue:
        current = queue.popleft()
        if current == end:
            break
        for dx, dy, direction in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < n and
                0 <= neighbor[1] < m and
                maze[neighbor[0]][neighbor[1]] != '#' and
                neighbor not in visited):
                
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = (current, direction)
    
    if end not in parent:
        return -1

    path = []
    step = end
    
    while step != start:
        prev_step, direction = parent[step]
        path.append(direction)
        step = prev_step

    path.reverse()
    return len(path), ''.join(path)

def main():
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]

    result = find_shortest_path(n, m, maze)

    if result == -1:
        print(-1)
    else:
        length, path = result
        print(length)
        print(path)

if __name__ == "__main__":
    main()