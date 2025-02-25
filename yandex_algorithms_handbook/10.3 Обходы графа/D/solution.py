from collections import deque
def bfs(start, end, maze, has_key=False):
    directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
    queue = deque([(start[0], start[1], '')])
    visited = set()
    visited.add((start[0], start[1]))
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return len(path), path

        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            cell = maze[nx][ny]

            if cell == '#' or (cell == 'D' and not has_key):
                continue

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + direction))

    return -1, ''

def find_shortest_path(maze, n, m):
    start, end, door, key = None, None, None, None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)
            elif maze[i][j] == 'D':
                door = (i, j)
            elif maze[i][j] == 'K':
                key = (i, j)

    result, path = bfs(start, end, maze)
    if result == -1:
        key_path, key_path_str = bfs(start, key, maze)
        end_path, end_path_str = bfs(key, end, maze, True)
        if key_path == -1 or end_path == -1:
            return -1, ''
        return key_path + 1 + end_path, key_path_str + 'P' + end_path_str
    return result, path

def main():
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]
    res = find_shortest_path(maze, n, m)
    if res[0] != -1:
        print(res[0])
        print(res[1])
    else:
        print(-1)

if __name__ == "__main__":
    main()