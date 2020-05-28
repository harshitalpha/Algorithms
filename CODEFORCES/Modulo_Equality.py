def compute_x(a, b, m):
    if a <= b:
        return b-a
    else:
        return (m+b)-a

n, m = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
dic_a = {}
dic_b = {}
for i in a:
    try:
        dic_a[i] = dic_a[i] + 1
    except KeyError:
        dic_a[i] = 1
for i in b:
    try:
        dic_b[i] = dic_b[i] + 1
    except KeyError:
        dic_b[i] = 1
if max(dic_a.items()) != 1:
    pass
else:
    mat = []
    for i in a:
        temp = []
        for j in b:
            temp.append(compute_x(i, j, m))
        mat.append(temp)
    


