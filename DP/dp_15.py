'''
    MAXIMUM LENGTH PAIR
'''
def solve(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i][0] not in d.keys():
            d[arr[i][0]] = arr[i][1]
    
    arr = []
    for i in sorted(d.keys()):
        arr.append([i,d[i]])
    
    print(arr)

    a = [arr[i][1] for i in range(len(arr))]

    print(a)

    dp = [0 for i in range(len(arr))]
    # for i in range(len(a)):
    #     m = 0
    #     for j in range(i):
    #         if a[j] <= a[i] and   :
    #             if dp[j] > m:
    #                 m = dp[j]
    #    dp[i] = m + 1    
    
    for i in range(len(arr)):
        m = 0
        for j in range(i):
            if arr[i][0] >= arr[j][1]:
                if dp[j] > m:
                    m = dp[j]
        dp[i] = m + 1
    print(dp)
    print(max(dp))




arr = [[5,24],[39,60],[15,28],[27,40],[50,90]]
solve(arr)