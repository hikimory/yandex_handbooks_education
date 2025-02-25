def find_winnable_games(nums, n, k):
    mid = nums[k-1]
    weak, strong = 0, 0
    for n in nums:
        if n < mid:
            weak += 1
        if n > mid:
            strong += 1
            
    games = 0
    while weak:
        if strong % 2:
            weak -= 1
        weak //= 2
        strong //= 2
        games += 1
    print(games)

def main():
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    find_winnable_games(nums, n, k)
if __name__ == "__main__":
    main()