n = int(input())
arr = [int(s) for s in input().split()]

arr.sort()

ans = []
ans.append(arr[n-1])
ans = ans + arr[:n-1]

for i in ans:
    print(i, end=" ")
print()