def count_inversions(arr, n):
    new_arr = arr.copy()
    return merge_sort_and_count(new_arr, 0, n - 1)

def merge_sort_and_count(arr, left, right):
    mid = (left + right) // 2
    inv_count = 0

    if left < right:
        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)

    return inv_count

def merge_and_count(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(0, n1):
        left_arr[i] = arr[left + i]

    for j in range(0, n2):
        right_arr[j] = arr[mid + 1 + j]

    i = j = 0
    k = left 
    inv_count = 0

    while i < n1 and j < n2:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            inv_count += (n1 - i)
        k += 1
    
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return inv_count

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    result = count_inversions(nums, n)
    print(result)

if __name__ == "__main__":
    main()