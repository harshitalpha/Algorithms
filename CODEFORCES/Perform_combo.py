t = int(input())
while(t):
    t=t-1
    n,m = [int(s) for s in input().split()]
    s = [ord(s) for s in input()]
    p = [int(s) for s in input().split()]

    # d = {}
    # for i in range(26):
    #     d[97+i] = 0

    # for i in s:
    #     d[i] += 1
    
    # for i in range(m):
    #     for j in range(p[i]):
    #         d[s[j]] += 1
    
    # for i in sorted(d.keys()):
    #     print(d[i], end=" ")
    # print()

    f = [1 for i in range(n)]
    for i in range(m):
        f[p[i] - 1] += 1
    
    # print(f)
    inc = 0
    for i in range(n-1,-1,-1):
        x = f[i]
        f[i] = f[i] + inc
        if x != 1:
            inc = inc + (x - 1)
    # pr    int(f)

    d = {}
    for i in range(26):
        d[97+i] = 0

    for i in range(n):
        d[s[i]] = d[s[i]] + f[i]

    for i in sorted(d.keys()):
        print(d[i], end=" ")
    print()