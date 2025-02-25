from functools import cmp_to_key

def largest_number(nums):
    def compare_numbers(a, b):
        return 1 if a + b < b + a else -1
    sorted_nums = sorted(nums, key=cmp_to_key(compare_numbers))
    return "0" if sorted_nums[0] == "0" else "".join(sorted_nums)

def main():
    n = int(input())
    nums = [x for x in input().split()]
    result = largest_number(nums)
    print(result) 

if __name__ == "__main__":
    main()