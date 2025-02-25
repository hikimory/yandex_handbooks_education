from collections import deque

def min_operations_bfs(X, Y):
    queue = deque([(X, 0)])
    visited = set([X])
    while queue:
        num, steps = queue.popleft()
        if num == Y:
            return steps
        for c in range(10):
            for op in [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]:
                new_num = op(num, c)
                if 0 <= new_num <= 10**5 and new_num not in visited:
                    queue.append((new_num, steps + 1))
                    visited.add(new_num)
    return -1

def main():
    X, Y = map(int, input().split())
    result = min_operations_bfs(X, Y)
    print(result)

if __name__ == "__main__":
    main()