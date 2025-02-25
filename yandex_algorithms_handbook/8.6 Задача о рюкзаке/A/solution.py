def knapsack(arr, weight, n):    
  dp = [[False] * (n + 1) for _ in range(weight + 1)]
  dp[0][0] = True
  for i in range(1, n + 1):
    for w in range(weight + 1):
      if arr[i-1] > w:
        dp[w][i] = dp[w][i - 1]
      else:
        dp[w][i] = (dp[w][i - 1] or dp[w - arr[i - 1]][i - 1])
  
  for w in range(weight, -1, -1):
    if dp[w][n] == True:
      return w
  return 0
  
def main():
  w, n = map(int, input().split())
  gold = [int(x) for x in input().split()]
  print(knapsack(gold, w, n))

if __name__ == "__main__":
  main()

