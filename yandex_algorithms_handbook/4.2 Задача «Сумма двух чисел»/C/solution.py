def main():
    n = int(input())
    a = input()
    b = input()
    print(''.join([a[i] + b[i] for i in range(n)]))
    
if __name__ == "__main__":
    main()