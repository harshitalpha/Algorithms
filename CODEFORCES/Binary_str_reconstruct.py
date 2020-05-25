import math
t = int(input())
while t:
    t = t-1
    n0, n1, n2 = [int(s) for s in input().split()]
    str1 = []
    for i in range(math.ceil(n1/2)):
        str1.append(0)
        str1.append(1)
    eve = 0
    if n1%2 == 0 and n1 > 0:
        eve = 1
    if len(str1) != 0:
        str0 = [0] * n0
        str2 = [1] * n2
        if eve == 0:
            ans = str0 + str1 + str2
        if eve == 1:
            ans = str0 + str1 + str2 + [0]
    else:
        if n0 != 0:
            ans = [0] * (n0 + 1)
        if n2 != 0:
            ans = [1] * (n2 + 1)

    for i in ans:
        print(i, end="")
    print()