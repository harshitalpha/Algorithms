t = int(input())
while(t):
    t=t-1
    n = int(input())
    b = [int(s) for s in input().split()]
    dic = [0]*((2*n)+1)
    for i in b:
        dic[i] = 1
    
    x = (2*n)+1
    a = []
    ans = 1
    # print(dic)
    for i in b:
        flag = 0
        # print(i)
        for j in range(i+1,x):
            if dic[j] == 0:
                # print("         {}".format(j))
                n = j
                dic[j] = 1
                flag = 1
                break
        # print(flag)
        # print(n)
        # print(dic)

        if flag == 0:
            ans = -1
            break
        else:
            a.append(i)
            a.append(n)
    
    if ans == 1:
        for i in a:
            print(i,end=" ")
        print()
    else:
        print(ans)



