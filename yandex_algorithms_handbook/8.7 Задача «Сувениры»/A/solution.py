def split(arr, n):    
    sum_arr = sum(arr)
    if (sum_arr % 3):
        return False
    V = sum_arr // 3
    dp = [[[False] * (V + 1) for _ in range(V + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        for s1 in range(V + 1):
            for s2 in range(V + 1):
                dp[i][s1][s2] = dp[i - 1][s1][s2]
                if s1 >= arr[i]:
                    dp[i][s1][s2] = dp[i][s1][s2] or dp[i - 1][s1 - arr[i]][s2]
                if s2 >= arr[i]:
                    dp[i][s1][s2] = dp[i][s1][s2] or dp[i - 1][s1][s2 - arr[i]]
    return dp[n][V][V]
  
def main():
  n = int(input())
  gold = [0] + [int(x) for x in input().split()]
  print(1 if split(gold, n) else 0)

if __name__ == "__main__":
    main()