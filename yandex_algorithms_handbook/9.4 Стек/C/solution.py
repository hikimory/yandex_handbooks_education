from collections import deque

def get_min_sum(n, k, a):
    total_min_sum = 0
    d = deque()

    for i in range(n):
        # Remove elements from the deck that are outside the window boundaries
        while d and d[0] < i - k + 1:
            d.popleft()

        # Remove elements from the deck that are greater than the current element to keep the deck in descending order
        while d and a[d[-1]] >= a[i]:
            d.pop()
        
        d.append(i)
        
        # If the window has reached length k, add the minimum to the total
        if i >= k - 1:
            total_min_sum += a[d[0]]
            
    print(total_min_sum)

def main():
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    get_min_sum(n, k, a)

if __name__ == "__main__":
    main()