def comb2(n, k):
    if k < 0 or n < 1:
        return 0

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    return factorial(k+n-1) // (factorial(k) * factorial(n-1))

def main():
    n, k = map(int, input().split())
    print(comb2(n, k))

if __name__ == "__main__":
    main()