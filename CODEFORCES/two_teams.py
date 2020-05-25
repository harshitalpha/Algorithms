t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]

    d = {}

    for i in a:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1

    max_size = d[a[0]]
    ele_in_sec_arr = a[0]
    for i in d.keys():
        if d[i] > max_size:
            max_size = d[i]
            ele_in_sec_arr = i
    
    count = 0
    for i in d.keys():
        if i is not ele_in_sec_arr:
            count = count + 1


    if count == max_size:
        print(max_size)
    elif count == max_size - 1:
        print(count)
    elif count <= max_size-2:
        print(count+1)
    elif count > max_size:
        print(max_size)


