def print_res(l, d, A, B):
  print(l)
  for i in range(l + 1):
    if i >= d:
      print(A[i] + B[i - d], end=' ')
    else:
      print(A[i], end=' ')

def main():
  a = int(input())
  A = [int(x) for x in input().split()]
  b = int(input())
  B = [int(x) for x in input().split()]

  if a >= b:
    print_res(a, abs(a-b), A, B)
  else:
    print_res(b, abs(a-b), B, A)

if __name__ == "__main__":
    main()