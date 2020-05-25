from operator import itemgetter
t = int(input())
while(t):
    t=t-1
    n = int(input())
    a = [ord(s) for s in input()]
    min_ele = 123
    min_i = -1
    for i in range(len(a)):
        if a[i] < min_ele:
            min_ele = a[i]
            min_i = i
    ans = min_i + 1
    k = ans - 1
    # print(ans)
    # print("K - {}".format(k))
    index_a = [i for i in range(n)]
    for i in range(n):
        index_a[i] = index_a[i] - k
    max_id = index_a[n-1]
    # print(index_a)
    zero_id = index_a.index(0)
    for i in range(0,zero_id):
        index_a[i] = max_id + 1
        max_id = max_id + 1
    # print(index_a)

    sort_t = []
    for i in range(n):
        sort_t.append((chr(a[i]), index_a[i]))
    
    # print(sort_t)

    x = sorted(sort_t, key = itemgetter(1))
    ans_arr = []
    for i in x:
        ans_arr.append(i[0])
    #print(x)
    # print(ans_arr)
    print("".join(ans_arr))
    print(ans)


