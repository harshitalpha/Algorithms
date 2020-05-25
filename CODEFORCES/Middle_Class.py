t = int(input())
while(t):
    t = t - 1
    n,x = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]

    s = 0
    count = 0
    for i in a:
        s = s + i
        if i >= x:
            count = count + 1
    
    a.sort()

    ans = 0
    if s/n >= x:
        ans = n
    else:
        for i in a[:n-1]:
            s = s - i
            n = n - 1
            if (s/n >= x):
                ans = n
                break

    print(max(count,ans))
        