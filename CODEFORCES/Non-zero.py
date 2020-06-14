t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    s = sum(arr)
    m = 1
    for i in arr:
        m = m * i
    if m != 0 and s != 0:
        print(0)
    elif m != 0 and s == 0:
        print(1)
    elif m == 0 and s != 0:
        count_zero = 0
        for i in arr:
            if i == 0:
                count_zero += 1
        if count_zero + s != 0:
            print(count_zero)
        else:
            print(count_zero + 1)
    else:
        count_zero = 0
        for i in arr:
            if i == 0:
                count_zero += 1
        print(count_zero)
