def lomuto_partition(array, low, high):
  if len(array) <= 1:
      return array
  pivot = array[low]
  i = low
  for j in range(low + 1, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i], array[low]) = (array[low], array[i])

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    lomuto_partition(arr, 0, n)
    print(*arr)
    
if __name__ == "__main__":
    main()