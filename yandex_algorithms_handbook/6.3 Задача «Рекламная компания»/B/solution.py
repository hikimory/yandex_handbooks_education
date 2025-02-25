def find_max_profit(data, n, w):
    data.sort(key=lambda x: x[0], reverse=True)
    nw = n * w
    max_profit = 0
    for ci, wi in data:
        if wi <= nw:
            nw -= wi
            max_profit += ci * wi
        else:
            max_profit += ci * nw
            break
    print(max_profit)

def main():
    n, k, w = map(int, input().split())
    data = []
    for _ in range(k):
        ci, wi = map(int, input().split())
        data.append((ci, wi))
    find_max_profit(data, n, w)
    
if __name__ == "__main__":
    main()
