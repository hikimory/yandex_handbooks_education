def binary_search_fisrt(arr, left, right, target):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def binary_search_last(arr, left, right, target):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_indexes(nums, queries):
    for q in queries:
        l = binary_search_fisrt(nums, 0, len(nums)-1, q)
        if l == -1:
            print(0, end=' ')
        else:
            r = binary_search_last(nums, 0, len(nums)-1, q)
            print(r - l + 1, end=' ')

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    m = int(input())
    queries = [int(x) for x in input().split()]
    find_indexes(nums, queries)

if __name__ == "__main__":
    main()