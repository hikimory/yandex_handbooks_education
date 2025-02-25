def HanoiTowers(n, fromPeg, auxPeg, toPeg):
  global l
  if n > 0:
    HanoiTowers(n - 1, fromPeg, toPeg, auxPeg)
    l.append(f"{fromPeg} {toPeg}")
    HanoiTowers(n - 1, auxPeg, fromPeg, toPeg)

l = []
def main():
    n = int(input())
    HanoiTowers(n, 1, 2, 3)
    print(len(l))
    print('\n'.join(l))

if __name__ == "__main__":
    main()