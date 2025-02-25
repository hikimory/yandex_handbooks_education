def binary_search(nums, low, high, q):
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == q:
            return mid
        elif nums[mid] < q:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    q = int(input())
    print(binary_search(nums, 0, len(nums)-1, q))

if __name__ == "__main__":
    main()