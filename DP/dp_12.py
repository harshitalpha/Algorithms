import sys
sys.setrecursionlimit(10**9)

'''
    Minimum Number Of Jumps To Reach End
'''

dp = {}
def solve(arr,i):
    n= len(arr)

    if arr[i] == 0 and i!= n-1:
        return -1

    if n-1 == i:
        dp[i] = 0
        return 0

    
    if i in dp.keys():
        return dp[i]
    else:
        m = list()
        for j in range(arr[i]):
            if j+i+1 < n:
                dp[j+i+1] = solve(arr,j+i+1)
                if dp[j+i+1] != -1:
                    m.append(dp[j+i+1])

        if len(m) != 0:
            dp[i] = min(m)+1
        if len(m) == 0:
            dp[i] = -1
        return dp[i]

arr =[1,2,1,2,0,2,6,7,6,8,0]
ans = solve(arr,0)
print(ans)


