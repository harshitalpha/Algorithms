t = int(input())
while(t):
    t=t-1
    n,a,b = [int(s) for s in input().split()]
    ans = [0]*n
    for i in range(b):
        ans[i] = chr(97+i)
    
    for j in range(i+1,a):
        ans[j] = ans[j-1]

    if(a == b):
        j = i

    x = 0
    for k in range(j+1,n):
        ans[k] = ans[x]
        x = x + 1

    for i in range(n):
        print(ans[i], end="")
    print()