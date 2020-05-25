t = int(input())
while(t):
    t = t - 1
    n = int(input())
    x = [int(s) for s in input()]

    a = [0]*n
    b = [0]*n

    a[0] = 1
    b[0] = 1

    f_one = n
    for i in range(n):
        if x[i] == 1:
            f_one = i
            a[f_one] = 1
            b[f_one] = 0
            x[f_one] = 0
            break

    

    for i in range(1,f_one):
        if x[i] == 2:
            a[i] = 1
            b[i] = 1
        else:
            a[i] = 0
            b[i] = 0
    
    for j in range(f_one):
        x[j] = b[j]
    
    for i in a:
        print(i,end="")
    print()
    for i in x:
        print(i,end="")
    print()
    # a = [1,0,0,0,0,0]
    # b = [1,0,0,0,0,0]
    # print(com_no(a,b))







