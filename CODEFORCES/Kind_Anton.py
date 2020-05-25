t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]

    minus = []
    plus = []
    zero = []

    if a[0] == 1:
        plus.append(1)
    else:
        plus.append(0)
    
    if a[0] == -1:
        minus.append(1)
    else:
        minus.append(0)
    
    if a[0] == 0:
        zero.append(1)
    else:
        zero.append(0)
    

    for i in range(1,n):
        if a[i] == -1:
            minus.append(1)
        else:
            minus.append(minus[i-1])
        if a[i] == 1:
            plus.append(1)
        else:
            plus.append(plus[i-1])
        if a[i] == 0:
            zero.append(1)
        else:
            zero.append(zero[i-1])

    ans = 1
    for i in range(n-1,0,-1):
        if b[i] == a[i]:
            continue
        elif b[i] > a[i]:
            if plus[i-1]:
                continue
            else:
                ans = 0
        elif b[i] < a[i]:
            if minus[i-1]:
                continue
            else:
                ans = 0
    
    if b[0] != a[0]:
        ans = 0

    if ans:
        print("YES")    
    else:
        print("NO")

        
