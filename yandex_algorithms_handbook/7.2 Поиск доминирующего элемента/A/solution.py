def find_majority_element(arr, n):
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return 1
    else:
        return 0

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    result = find_majority_element(nums, n)
    print(result)

if __name__ == "__main__":
    main()