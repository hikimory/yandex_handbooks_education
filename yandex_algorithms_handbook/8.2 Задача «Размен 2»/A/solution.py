import math

def optimal_exchange(money):
    coins = [1, 3, 4]
    end = money + 1
    table = [math.inf for _ in range(end)]
    table[0] = 0
    for m in range(1, end):
        for c in coins:
            if c <= m:
                table[m] = min(table[m], 1 + table[m-c])
    return table[money]

def main():
    money = int(input())
    print(optimal_exchange(money))

if __name__ == "__main__":
    main()
