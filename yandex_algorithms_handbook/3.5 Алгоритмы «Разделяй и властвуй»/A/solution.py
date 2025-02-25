def selection_sort(n, arr):
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    selection_sort(n, arr)
    print(*arr)

if __name__ == "__main__":
    main()