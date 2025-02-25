def find_combinations(arr, capacity):
    data = sorted(arr, key=lambda x: x[0] / x[1], reverse=True)
    cash = 0
    while capacity > 0 and data:
        price, weight = data.pop(0)
        if weight <= capacity:
            capacity -= weight
            cash += price
        else:
            cash += price * capacity / weight
            break
    print(f"{cash:.3f}")

def main():
    n, capacity = map(int, input().split())
    data = []
    for _ in range(n):
        price, weight = map(int, input().split())
        data.append((price, weight))
    find_combinations(data, capacity)

if __name__ == "__main__":
    main()