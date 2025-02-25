def GCD(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a,b)

def LCM(a, b):
    return a*b//GCD(a, b)

def main():
    a, b = map(int, input().split())
    print(LCM(a, b))

if __name__ == "__main__":
    main()