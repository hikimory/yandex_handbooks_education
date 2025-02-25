def gcd_reverse(n):
    a, b = 1, 0
    while a + b <= n:
        if a > b:
            b += a
        else:
            a += b
    return min(a, b), max(a, b)

def main():
    n = int(input())
    a, b = gcd_reverse(n)
    print(f"{a} {b}")

if __name__ == "__main__":
    main()