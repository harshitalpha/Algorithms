t = int(input())
while(t):
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    ans = [-1 for i in range(n)]
    i = 0
    j = n-1
    max_ele = n
    while i<=j:
        l = arr[i]
        r = arr[j]
        if l == max_ele:
            if ans[l-1] == -1:
                ans[l-1] = 1
            i += 1
        elif r == max_ele:
            if ans[r-1] == -1:
                ans[r-1] = 1
            j -= 1
        else:
            if l > r:
                if ans[l-1] == -1:
                    length = j-i+1
                    for k in range(l,length):
                        if ans[k-1] == -1:
                            ans[k-1] = 0
                        if ans[length-1] == -1:
                            ans[length-1] = 1
                i += 1
            else:
                if ans[r-1] == -1:
                    length = j-i+1
                    for k in range(r,length):
                        if ans[k-1] == -1:
                            ans[k-1] = 0
                        if ans[length-1] == -1:
                            ans[length-1] = 1

                j -= 1
        max_ele = max_ele - 1
    for i in ans:
        print(i, end="")
    print()
