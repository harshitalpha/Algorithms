t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    for i in range(n):
        x = arr[i]
        if x == 1:
            first_occur = 1
            flag = "min"
            first_occur_idx = i
            break
        if x == n:
            first_occur = n
            flag = "max"
            first_occur_idx = i
            break

    ans = [first_occur]
    for i in range(first_occur_idx, n):
        x = arr[i]
        if flag == "min":
            if x == n:
                ans.append(x)
                sec_occ_idx = i
                break
        if flag == "max":
            if x == 1:
                ans.append(x)
                sec_occ_idx = i
                break
    ans = ans + arr[i+1:]
    print(len(ans))
    print(*ans)