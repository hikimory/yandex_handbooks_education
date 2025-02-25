def levenshtein(str1, n, str2, m):
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    
    l = n + 1
    current_row = [0] * l
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [0] * l
        for j in range(1, n + 1):
            add, delete, match = previous_row[j], current_row[j - 1], previous_row[j - 1]
            if str1[j - 1] == str2[i - 1]:
                match += 1
            current_row[j] = max(add, delete, match)

    return current_row[n]

def main():
    n = int(input())
    str1 = [int(x) for x in input().split()]
    m = int(input())
    str2 = [int(x) for x in input().split()]
    print(levenshtein(str1, n, str2, m))

if __name__ == "__main__":
    main()