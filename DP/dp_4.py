'''
    COUNT SUBARRAY
    https://www.codechef.com/problems/SUBINC
'''
def solve_n_2_time(a,n):
    mat = [[False for i in range(n)] for j in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                if i == j:
                    mat[i][j] = True
                    count = count + 1
                else:
                    if(mat[j-1][i] == True):
                        if(a[j] >= a[j-1]):
                            mat[j][i] = True
                            count = count + 1
                        else:
                            mat[j][i] = False
                    else:
                        mat[j][i] = False
    
    return count

def solve_n_time(a,n):
    b = [1 for i in range(n)]
    for i in range(1,n):
        if a[i] >= a[i-1]:
            b[i] = b[i-1] + 1

    return sum(b) 

t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    ans = solve_n_2_time(a,n)
    ans_1 = solve_n_time(a,n)
    print(ans)
    print(ans_1)

