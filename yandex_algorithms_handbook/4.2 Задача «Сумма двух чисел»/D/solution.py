def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def print_matrix(matrix, n, k):
    for i in range(n):
        for j in range(k):
            print(matrix[i][j], end=' ')
        print()

def sum_matrices(m1, m2, n, k):
    res = [[m1[i][j] + m2[i][j] for j in range(k)] for i in range(n)]
    return res

def main():
    n, k = map(int, input().split())
    m_A = read_matrix(n)
    m_B = read_matrix(n)
    res = sum_matrices(m_A, m_B, n, k)
    print_matrix(res, n, k)
    
if __name__ == "__main__":
    main()