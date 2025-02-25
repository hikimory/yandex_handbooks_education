def main():
    n = int(input())
    numbers = set()
    answer = []
    for _ in range(n):
        q, num = input().split()
        if q == '1':
            numbers.add(num)
        elif q == '2':
            if num in numbers:
                answer.append('1')
            else:
                answer.append('0')

    print('\n'.join(answer))

if __name__ == "__main__":
    main()