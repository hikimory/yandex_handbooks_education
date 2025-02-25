from collections import deque
def find_shortest_path(n, m, maze, key_door_map):
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)

    if not start or not end:
        return -1

    door_to_key = {door: key for door, key in key_door_map}
    key_to_door = {key: door for door, key in key_door_map}
    queue = deque([(start[0], start[1], frozenset(), "")])  # (x, y, keys, path)
    visited = set()
    while queue:
        x, y, keys, path = queue.popleft()
        if (x, y, keys) in visited:
            continue
        visited.add((x, y, keys))
        if (x, y) == end:
            return len(path), path
        for dx, dy, move in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                cell = maze[nx][ny]
                if cell == '#':
                    continue
                if cell in door_to_key and door_to_key[cell] not in keys:
                    continue
                queue.append((nx, ny, keys, path + move))
        if maze[x][y] in key_to_door and maze[x][y] not in keys:
            new_keys = keys | {maze[x][y]}
            queue.append((x, y, new_keys, path + "P"))
    return -1

def main():
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]
    k = int(input())
    key_door_map = [input().split() for _ in range(k)]
    result = find_shortest_path(n, m, maze, key_door_map)
    if result == -1:
        print(-1)
    else:
        distance, path = result
        print(distance)
        print(path)
        
if __name__ == "__main__":
    main()
