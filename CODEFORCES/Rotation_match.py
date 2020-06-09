n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
d = {}
for i in range(n):
    d[b[i]] = i
jump_needed = []
for i in range(n):
    map_idx = d[a[i]]
    if i <= map_idx:
        jump_needed.append(map_idx - i)
    else:
        x = ((n-1)-i) + map_idx + 1
        jump_needed.append(x)
di = {}
for i in jump_needed:
    try:
        di[i] = di[i] + 1
    except KeyError:
        di[i] = 1
print(max(di.values()))
