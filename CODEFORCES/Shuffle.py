t = int(input())
while t:
    t -= 1
    n, x, m = [int(s) for s in input().split()]
    mat = []
    for i in range(m):
        mat.append([int(s) for s in input().split()])
    cur_range = [x, x]
    for i in range(m):
        cur_l = mat[i][0]
        cur_r = mat[i][1]
        if (cur_range[0] >= cur_l and cur_range[0] <= cur_r) or (cur_range[1] >= cur_l and cur_range[1] <= cur_r):
            cur_range[0] = min(cur_l, cur_range[0])
            cur_range[1] = max(cur_r, cur_range[1])
        else:
            pass
        # print(cur_range)
    ans = cur_range[1] - cur_range[0] + 1
    print(ans)