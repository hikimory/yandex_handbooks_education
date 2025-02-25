def find_count(arr, cash):
    prices = sorted(arr)
    count = 0
    for price in prices:
        if cash >= price:
            count = count + 1
            cash = cash - price
    print(count)

def main():
    n, cash = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(int(input()))
    find_count(data, cash)

if __name__ == "__main__":
    main()