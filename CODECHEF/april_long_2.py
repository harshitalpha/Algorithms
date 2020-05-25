t  =int(input())
while t:
    t = t - 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    arr.sort(reverse=True)
    cost = 0
    dec = 0
    for i in arr:
        if(i != 0):
            cost = cost + i - dec
            dec = dec + 1
        else:
            break
    
    print(cost)
