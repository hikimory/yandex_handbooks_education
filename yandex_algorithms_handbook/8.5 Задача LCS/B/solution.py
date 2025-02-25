def levenshtein(str1, l1, str2, l2, str3, l3):
    dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            for k in range(1, l3 + 1):
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
                if str1[i - 1] == str2[j - 1] and str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] + 1)
    return dp[l1][l2][l3]

def main():
    l1 = int(input())
    str1 = [int(x) for x in input().split()]
    l2 = int(input())
    str2 = [int(x) for x in input().split()]
    l3 = int(input())
    str3 = [int(x) for x in input().split()]
    print(levenshtein(str1, l1, str2, l2, str3, l3))

if __name__ == "__main__":
    main()