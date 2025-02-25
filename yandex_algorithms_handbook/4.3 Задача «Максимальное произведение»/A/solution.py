def MaxProduct(A):
  sorted_numbers = sorted(A)
  return sorted_numbers[-1] * sorted_numbers[-2]

def main():
  a = int(input())
  A = [int(x) for x in input().split()]
  print(MaxProduct(A))

if __name__ == "__main__":
    main()
