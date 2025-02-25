def getCountIntervals(intervals):
    lastEndTime = -1
    count = 0
    intervals.sort(key=lambda x: x[1])

    for start, end in intervals:
        if start > lastEndTime:
            count += 1
            lastEndTime = end
    return count

def main():
    num_intervals = int(input())
    intervals = []
    for _ in range(num_intervals):
        start, end = map(int, input().split())
        intervals.append((start, end))

    print(getCountIntervals(intervals))

if __name__ == "__main__":
    main()