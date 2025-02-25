def min_coins(money):
    coins = [50, 20, 10, 5, 1]
    result = []
    i = 0
    while money > 0:
        while money >= coins[i]:
            money -= coins[i]
            result.append(coins[i])
        i += 1
    return result

def main():
    m = int(input())
    res = min_coins(m)
    print(len(res))
    print(*res)

if __name__ == "__main__":
    main()