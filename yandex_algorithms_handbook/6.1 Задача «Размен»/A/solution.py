def find_combinations(n):
    combinations = []
    for tens in range(n // 10 + 1):
        remaining_after_tens = n - tens * 10
        for fives in range(remaining_after_tens // 5 + 1):
            remaining_after_fives = remaining_after_tens - fives * 5
            ones = remaining_after_fives
            combinations.append((tens, fives, ones))
    return combinations

def print_combinations(combinations):
    print(f"{len(combinations)}")
    for arr in combinations:
        tens, fives, ones = arr
        count = tens + fives + ones
        res = f" ".join(["10"] * tens + ["5"] * fives + ["1"] * ones)
        print(f"{count} {res}")

def main():
    n = int(input())
    combinations = find_combinations(n)
    print_combinations(combinations)

if __name__ == "__main__":
    main()