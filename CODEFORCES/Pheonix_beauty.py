def all_done(d):
    ans = 1
    for i in d.keys():
        if d[i] == 0:
            ans = 0
            break
    return ans

t = int(input())
while t:
    t = t - 1
    n,k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    if n == k:
        print(n)
        for i in a:
            print(i,end=" ")
        print()
    else:
        d = {}
        for i in a:
            try:
                d[i] = d[i] + 1
            except KeyError:
                d[i] = 1
        if len(d) > k:
            print(-1)
        else:
            ans = []
            total_subsequence = n-k+1
            index = 0
            dic = {}
            for i in d.keys():
                dic[i] = 0
            for i in range(k):
                if dic[a[index]] == 0:
                    ans.append(a[index])
                    dic[a[index]] = 1
                    index = index + 1
                    continue
                else:
                    if all_done(dic) == 0:
                        for i in dic.keys():
                            if dic[i] == 0:
                                ans.append(i)
                                dic[i] = 1
                                break
                    else:
                        ans.append(a[index])
                        index = index + 1
            dic = {}
            for i in range(k):
                try:
                    dic[ans[i]] = dic[ans[i]] + 1
                except KeyError:
                    dic[ans[i]] = 1
            it = 1
            while index != n:
                temp_d = dic.copy()
                x = it
                for i in range(k-1):
                    temp_d[ans[x]] = temp_d[ans[x]] - 1
                    x = x + 1
                for i in temp_d.keys():
                    if temp_d[i] != 0:
                        next_ele = i
                        break
                if next_ele == a[index]:
                    ans.append(next_ele)
                    index = index + 1
                else:
                    ans.append(next_ele)
                it = it + 1
            print(len(ans))
            for i in ans:
                print(i, end=" ")
            print()