def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[len(array) // 2]
  left = [x for x in array if x < pivot]
  middle = [x for x in array if x == pivot]
  right = [x for x in array if x > pivot]

  return quick_sort(left) + middle + quick_sort(right)

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    sorted_arr = quick_sort(arr)
    print(*sorted_arr)
    
if __name__ == "__main__":
    main()
