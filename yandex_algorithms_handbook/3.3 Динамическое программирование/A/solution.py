def rocks(n, m):
    R = [[False] * (m + 1) for _ in range(n + 1)]

    # Fill the first row
    for i in range(1, n + 1):
        R[i][0] = False if R[i - 1][0] else True

    # Fill the first column
    for j in range(1, m + 1):
        R[0][j] = False if R[0][j - 1] else True

    # Fill the rest of the matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if R[i - 1][j - 1] and R[i][j - 1] and R[i - 1][j]:
                R[i][j] = False
            else:
                R[i][j] = True

    return "Win" if R[n][m] else "Lose"

def rocks2(n, m):
    if n % 2 == 0 and m % 2 == 0:
        print('Loose')
    else:
        print('Win')

def main():
    n, m = map(int, input().split())
    print(rocks(n, m))

if __name__ == "__main__":
    main()