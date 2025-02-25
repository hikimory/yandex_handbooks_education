# F2015mod3 = 251⋅8+7
# 8 - period length
# 2015 % 8 = 7 -> F2015mod3 = F7mod3

def pisano_period(m):
    a, b = 0, 1
    period = 0
    while True:
        a, b = b, (a + b) % m
        period += 1
        if a == 0 and b == 1:
            return period

def fibonacci_mod(n, m):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % m
    return curr

def main():
    n, m = map(int, input().split())
    period = pisano_period(m)
    n %= period
    print(fibonacci_mod(n, m))

if __name__ == "__main__":
    main()