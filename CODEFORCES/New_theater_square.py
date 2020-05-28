import math
t = int(input())
while t:
    t = t - 1
    n, m, x, y = [int(s) for s in input().split()]
    mat = []
    for i in range(n):
        mat.append(input())
    if y >= 2*x:
        prefer = 1
    else:
        prefer = 2
    cost = 0
    for i in range(n):
        if mat[i][0] == '.':
            arr = [1]
        else:
            arr = []
        for j in range(1, m):
            if mat[i][j] == '.' and mat[i][j-1] == '.':
                arr[-1] = arr[-1] + 1
            if mat[i][j] == '.' and mat[i][j-1] == '*':
                arr.append(1)

        # print(arr)
        if prefer == 1:
            cost = cost + sum(arr) * x
        if prefer == 2:
            for k in arr:
                cost = cost + (math.floor(k/2)) * y + (k - 2 * math.floor(k/2)) * x
        # print(cost)
    print(cost)
