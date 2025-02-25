def rocks(n, m):
    if n == m:
        return "Lose"
    elif abs(n - m) % 3 == 0:
        return "Lose"
    else:
        return "Win"

def main():
    n, m = map(int, input().split())
    print(rocks(n, m))

if __name__ == "__main__":
    main()