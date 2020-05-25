t = int(input())
while t:
    t = t - 1
    n, m = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    d = {}
    for i in range(n):
        d[a[i]] = i+1
    position_a = []
    for i in b:
        position_a.append(d[i])
    total_time = 0
    pos_grater = 0
    item_gone = 0
    # print(position_a)
    for i in position_a:
        if i > pos_grater:
            total_time = total_time + 2*(i-item_gone-1)  + 1
            pos_grater = i
            item_gone = item_gone + 1
        else:
            total_time = total_time + 1
            item_gone = item_gone + 1

    print(total_time)
