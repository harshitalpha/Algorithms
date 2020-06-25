import sys
sys.setrecursionlimit(10**9)
'''
    COIN CHANGE
'''
dp = {}
def solve(arr,start,end,coin):
    # print("Coin : {}".format(coin))
    # print("Start : {}".format(start))
    # print("End : {}".format(end))
    # print("\n")
    if (coin == 0):
        return 1
    if (start > end):
        return 0
    if (coin < 0):
        return 0
    else:
        if (end,coin) in dp:
            return dp[(end,coin)]
        else:
            x =  solve(arr, start, end-1, coin) + solve(arr, start, end, coin - arr[end])
            dp[(end,coin)] = x
            return x


def solve_bottum_up(arr,coin):
    r = len(arr) + 1
    c = coin+1
    mat = [[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        mat[i][0] = 1
    

    for i in range(1,r):
        for j in range(1,c):
            x = mat[i][j-arr[i-1]] if j-arr[i-1]>=0 else 0
            mat[i][j] = x + mat[i-1][j]
        
    return mat[r-1][c-1]

arr = [1,2,3]
coin = 1000000
ans = solve(arr,0,len(arr)-1,coin) 
print(ans)
ans = solve_bottum_up(arr, coin)
print(ans)


