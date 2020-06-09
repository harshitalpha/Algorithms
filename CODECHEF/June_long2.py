for _ in range(int(input())):
    s = [s for s in input()]
    n = len(s)
    i = 0
    count = 0
    while i < n-1:
        cur_stu = s[i]
        if i+1 < n:
            next_stu = s[i+1]
            if next_stu != cur_stu:
                i = i + 2
                count = count + 1
            else:
                i += 1
        else:
            break
    print(count)