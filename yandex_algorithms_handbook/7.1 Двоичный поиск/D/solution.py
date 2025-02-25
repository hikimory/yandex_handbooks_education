def can_cover(points, k, length):
    used = 0
    last = 0
    for point in points:
        if point > last:
            used += 1
            last = point + length
        if used > k:
            return False
    return True

def find_min_length(points, k):
    points.sort()
    left, right = 0, points[-1] - points[0]
    while left < right:
        mid = (left + right) // 2
        if can_cover(points, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

def main():
    n, k = map(int, input().split())
    points = list(map(int, input().split()))
    result = find_min_length(points, k)
    print(result)

if __name__ == "__main__":
    main()