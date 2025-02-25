def MaxProduct3(A):
    if len(A) == 3:
        print(A[0] * A[1] * A[2])
    else:
        A.sort()
        prod1 = A[-1] * A[-2] * A[-3]
        prod2 = A[0] * A[1] * A[-1]
        print(max(prod1, prod2))

def main():
    a = int(input())
    A = [int(x) for x in input().split()]
    MaxProduct3(A)

if __name__ == "__main__":
    main()