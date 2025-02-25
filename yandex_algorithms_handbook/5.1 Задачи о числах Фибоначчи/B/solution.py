def fibonacci_last_digit(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr

def main():
    n = int(input())
    print(fibonacci_last_digit(n))

if __name__ == "__main__":
    main()