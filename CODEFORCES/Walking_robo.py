t = int(input())
while t:
    t = t - 1
    n = int(input())
    string = [s for s in input()]
    dictonary = dict()
    x = 0
    y = 0
    dictonary[(0,0)] = 0
    current_max_len = float('inf')
    l = 0
    r = 0
    for i in range(n):
        s = string[i]
        if s == 'R':
            x = x + 1
            if (x,y) in dictonary.keys():
                length = (i+1) - dictonary[(x,y)]
                if length < current_max_len:
                    current_max_len = length
                    l = dictonary[(x,y)] + 1
                    r = i + 1
            dictonary[(x,y)] = i + 1

        if s == 'L':
            x = x - 1
            if (x, y) in dictonary.keys():
                length = (i + 1) - dictonary[(x, y)]
                if length < current_max_len:
                    current_max_len = length
                    l = dictonary[(x, y)] + 1
                    r = i + 1
            dictonary[(x, y)] = i + 1

        if s == 'U':
            y = y + 1
            if (x, y) in dictonary.keys():
                length = (i + 1) - dictonary[(x, y)]
                if length < current_max_len:
                    current_max_len = length
                    l = dictonary[(x, y)] + 1
                    r = i + 1
            dictonary[(x, y)] = i + 1

        if s == 'D':
            y = y - 1
            if (x, y) in dictonary.keys():
                length = (i + 1) - dictonary[(x, y)]
                if length < current_max_len:
                    current_max_len = length
                    l = dictonary[(x, y)] + 1
                    r = i + 1
            dictonary[(x, y)] = i + 1

    # print(dictonary)
    if l == 0 and r == 0:
        print("-1")
    else:
        print(l, end=" ")
        print(r)