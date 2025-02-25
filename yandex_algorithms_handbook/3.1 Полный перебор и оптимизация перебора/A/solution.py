def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def main():
    n = int(input())
    print(factorial_iterative(n))

if __name__ == "__main__":
    main()
