t = int(input())
while t:
    t = t - 1
    n = int(input())
    x = [int(s) for s in input().split()]
    dis = [0]
    for i in range(1,n):
        dis.append(x[i]-x[i-1])
    # print(dis)
    arr = []
    count = 0
    for i in dis:
        if i == 1 or i == 2:
            count = count + 1
        else:
            if count is not 0:
                arr.append(count)
            count = 1
    if count is not 0:
        arr.append(count)
    if len(arr) == 0:
        arr = [0]
    # print(arr)
    m = min(arr)
    ma = max(arr)
    print(m,ma)
