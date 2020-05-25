t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    dis = []
    for i in range(len(a)):
        if a[i] == 1:
            dis.append(i)
    
    if len(dis) == 1:
        print("YES")
    else:
        sub = []
        for i in range(1,len(dis)):
            sub.append(dis[i] - dis[i-1])
        flag = 1
        for i in sub:
            if i < 6:
                flag = 0
                break
        if flag:
            print("YES")
        else:
            print("NO")