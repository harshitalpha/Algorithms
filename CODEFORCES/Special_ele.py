t = int(input())
while t:
    t = t-1
    n = int(input())
    arr = [int(s) for s in input().split()]

    mat =[[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        mat[i][i] = arr[i]

    count = 0
    exist = {}
    for i in range(n-1):
        for j in range(i+1, n):
            mat[i][j] = mat[i][j-1] + arr[j]
            exist[mat[i][j]] = 1

    for i in arr:
        try:
            x = exist[i]
            count = count + 1
        except KeyError:
            continue
    # print(mat)
    print(count)

