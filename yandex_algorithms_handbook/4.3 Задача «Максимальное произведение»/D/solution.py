def MaxProduct4(A):
    if len(A) == 4:
        print(A[0] * A[1] * A[2]* A[3])
    else:
        A.sort()
        prod1 = A[-1] * A[-2] * A[-3] * A[-4]
        prod2 = A[-1] * A[-2] * A[-3] * A[0]
        prod3 = A[-1] * A[-2] * A[0] * A[1]
        prod4 = A[0] * A[1] * A[2]* A[3]
        print(max(prod1, prod2, prod3, prod4))

def main():
    a = int(input())
    A = [int(x) for x in input().split()]
    MaxProduct4(A)

if __name__ == "__main__":
    main()