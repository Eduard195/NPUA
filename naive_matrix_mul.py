a = [[2, 3, 5],
     [4, 5, 6],
     [1, 9, 7]]

b = [[1, 4, 9],
     [4, 0, 8],
     [7, 5, 3]]



def naive_matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c

print(naive_matrix_multiply(a, b))

