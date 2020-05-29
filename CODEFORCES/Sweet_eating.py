n, m = [int(s) for s in input().split()]
arr = [int(s) for s in input().split()]
arr.sort()
sum = 0
running_sum = [0] * n
for i in range(m):
    sum = sum + arr[i]
    running_sum[i] = sum
for i in range(m, n):
    running_sum[i] = running_sum[i-1] + arr[i] - arr[i-m]
ans = []
for i in range(n):
    ans_i = running_sum[i]
    if i-m >= 0:
        ans_i = ans_i + 2*ans[i-m]
    if i-(2*m) >= 0:
        ans_i = ans_i - ans[i-(2*m)]
    ans.append(ans_i)
print(*ans)


