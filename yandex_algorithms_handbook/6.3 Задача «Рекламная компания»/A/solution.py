def find_max_value(p, c, n):
    p.sort()
    c.sort()
    val = 0
    for i in range(n):
        val = val + p[i]*c[i]
    print(val)

def main():
    n = int(input())
    prices = [int(x) for x in input().split()]
    clicks = [int(x) for x in input().split()]
    find_max_value(prices, clicks, n)

if __name__ == "__main__":
    main()