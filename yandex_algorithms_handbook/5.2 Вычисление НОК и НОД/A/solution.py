def GCD(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a,b)

def main():
    a, b = map(int, input().split())
    print(GCD(a, b))

if __name__ == "__main__":
    main()