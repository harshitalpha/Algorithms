s = [s for s in input()]

d = {}
for i in s:
    d[i] = [0]

for i in range(len(s)):
    for j in d.keys():
        if j == s[i]:
            d[j].append(d[j][len(d[j])-1] + 1)
        else:
            d[j].append(d[j][len(d[j]) - 1])
# print(d)

ans = {}
for i in range(len(s)):
    l = s[i]
    id = i+1
    try:
        ans[l] = ans[l] + 1
    except KeyError:
        ans[l] = 1

    for j in d.keys():
        if j == l:
            if d[j][id]-1 > 0:
                new_str = j+l
                # print(new_str)
                try:
                    ans[new_str] = ans[new_str] + d[j][id] - 1
                except KeyError:
                    ans[new_str] = d[j][id]- 1
        else:
            if d[j][id] > 0:
                new_str = j+l
                # print(new_str)
                try:
                    ans[new_str] = ans[new_str] + d[j][id]
                except KeyError:
                    ans[new_str] = d[j][id]

# print(ans)
max_ele = 0
for i in ans:
    if ans[i] > max_ele:
        max_ele = ans[i]
print(max_ele)