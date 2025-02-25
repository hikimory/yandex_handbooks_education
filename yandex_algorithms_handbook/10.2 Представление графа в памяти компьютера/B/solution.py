def main():
    n, m = map(int, input().split())
    room = [[-1] * (m + 2) for _ in range(n + 2)]
    """
    -1 = клетка, по которой НЕЛЬЗЯ перемещаться (#)
    0 = клетка, по которой МОЖНО перемещаться (.)
    1 = клетка, по которой прошли
    """
    for row in range(1, n + 1):
        line = input()
        for piece in range(1, m + 1):
                if line[piece - 1] == '.':
                    room[row][piece] = 0
    
    start_row, start_col = map(int, input().split())
    robot = [start_row, start_col]
    room[robot[0]][robot[1]] = 1
    direction = 0
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    amount_moves = int(input())
    moves = input()
    answer = 1
    for step in moves:
        if step == 'R':
            direction = (direction + 1) % 4
        elif step == 'L':
            direction = (direction - 1) % 4
        elif step == 'M':
            to_row = robot[0] + drow[direction]
            to_col = robot[1] + dcol[direction]
            if room[to_row][to_col] in (0, 1):
                if room[to_row][to_col] == 0:
                    room[to_row][to_col] = 1
                    answer += 1
                robot[0] += drow[direction]
                robot[1] += dcol[direction]
    print(answer)
if __name__ == "__main__":
    main()