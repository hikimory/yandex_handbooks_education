def min_segments(points, n, l):
    points.sort()
    count = 1
    min_val = points[0]
    for i in range(1, n):
        if abs(min_val - points[i]) > l:
            count += 1
            min_val = points[i]
    return count

def main():
    n, l = map(int, input().split())
    points = [int(x) for x in input().split()]
    result = min_segments(points, n, l)
    print(result) 

if __name__ == "__main__":
    main()