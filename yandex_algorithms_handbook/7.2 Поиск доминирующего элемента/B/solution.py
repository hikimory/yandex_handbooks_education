def find_majority_element(nums,k):
    hash = {}    
    for n in nums:
        hash[n] = 1 + hash.get(n, 0)
    
    count = 0
    size = k // 4
    for value in hash.values():
        if value > size:
            count +=1
            if count == 3:
                return 1
    return 0

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    result = find_majority_element(nums, n)
    print(result)

if __name__ == "__main__":
    main()