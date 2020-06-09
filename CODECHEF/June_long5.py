for _ in range(int(input())):
    n = int(input())
    mat = [[0 for i in range(n)] for j in range(n)]
    odd = 1
    even = 2
    for i in range(n):
        for j in range(n):
            if i%2 == 0:
                if j%2 == 0:
                    mat[i][j] = odd
                    odd += 2
                else:
                    mat[i][j] = even
                    even += 2
            else:
                if j%2 == 1:
                    mat[i][j] = odd
                    odd += 2
                else:
                    mat[i][j] = even
                    even += 2
    for i in range(n):
        print(*mat[i])