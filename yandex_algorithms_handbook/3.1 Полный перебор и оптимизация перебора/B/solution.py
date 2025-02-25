def comb(n, k):
    if k > n:
        return 0

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    return factorial(n) // (factorial(k) * factorial(n-k))

def main():
    n, k = map(int, input().split())
    print(comb(n, k))

if __name__ == "__main__":
    main()
