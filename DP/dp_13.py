'''
    Longest Increasing SubSequence
'''
def solve(arr):
    dp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        m = 0
        for j in range(i):
            if arr[j] <= arr[i]:
                if dp[j] > m:
                    m = dp[j]
        
        dp[i] = m + 1    
    #print(dp)
    return max(dp), dp

def get_sequence(arr,dp):
    x = max(dp)
    i = dp.index(x)
    seq_id = [i]
    for j in range(i,-1,-1):
        if dp[j] == x - 1:
            x = dp[j]
            seq_id.append(j)
    seq = []
    for i in seq_id:
        seq.append(arr[i])
    return seq


arr = [10,22,9,33,21,50,41,60,80]
ans,dp = solve(arr)
print(ans)
seq = get_sequence(arr,dp)
print(seq)
