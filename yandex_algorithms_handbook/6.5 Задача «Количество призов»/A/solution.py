def is_correct(k, n):
    return (k*(k+1) // 2) <= n

def find_count_presents(n):
    low, high = 0, n
    k = 1
    while low < high:
        k = (low + high) // 2
        if is_correct(k, n):
            low = k + 1
        else:
            high = k
    return low - 1

def main():
    n = int(input())
    print(find_count_presents(n)) 

if __name__ == "__main__":
    main()