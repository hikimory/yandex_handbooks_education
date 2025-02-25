def main():
    n, m = map(int, input().split())
    graph1 = [[0] * (n + 1) for _ in range(n + 1)] 
    graph2 = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        row = [int(x) for x in input().split()[1:]]
        l = len(row)
        if l > 1:
            for i in range(1, l):
                graph1[row[i - 1]][row[i]] = 1
                graph1[row[i]][row[i - 1]] = 1

            for i in range(l):
                for j in range(l):
                    if i != j:
                        graph2[row[i]][row[j]] = 1

    for i in range(1, n + 1):
        print(' '.join(str(graph1[i][j]) for j in range(1, n + 1)))
    for i in range(1, n + 1):
        print(' '.join(str(graph2[i][j]) for j in range(1, n + 1)))

if __name__ == "__main__":
    main()
