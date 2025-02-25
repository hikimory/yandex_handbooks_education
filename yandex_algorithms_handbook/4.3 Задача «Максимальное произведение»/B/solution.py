def answer(n):
  #1.5n > 1 + 2(n-2) -> n > 6
  if n < 7:
      print("No")
  else:
      print("Yes")
      print(n)
      for i in range(1, n):
        print(i, end=' ')
def main():
  n = int(input())
  answer(n)

if __name__ == "__main__":
    main()