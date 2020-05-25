import math
t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    
    a.sort()

    ans = []
    dif = []

    s = int(math.ceil(n/2) - 1)

    ans.append(a[s])
    r = s + 1
    l = s - 1
    while(r <= n-1 and l >= 0):
        ans.append(a[r])
        ans.append(a[l])
        r = r + 1
        l = l - 1
    
    if r == n-1:
        ans.append(a[r])
    
    for i in ans:
        print(i, end=" ")
    print()
    

