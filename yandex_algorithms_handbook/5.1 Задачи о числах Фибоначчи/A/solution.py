def fibonacci(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()
