def find_points(data, n):
    data.sort(key=lambda x: x[1])
    min_r = data[0][1]
    points = [min_r]
    for i in range(1, n):
        if min_r > data[i][1] or min_r < data[i][0]:
            min_r = data[i][1]
            points.append(min_r)
    print(len(points))
    print(*points)

def main():
    n = int(input())
    data = []
    for _ in range(n):
        l, r = map(int, input().split())
        data.append((l, r))
    find_points(data, n)

if __name__ == "__main__":
    main()