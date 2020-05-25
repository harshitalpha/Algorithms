t = int(input())
while(t):
    t = t - 1
    n = int(input())
    mat =  []
    for i in range(n):
        mat.append([int(s) for s in input().split()])
    
    not_marrid = []
    b = {}
    for i in range(n):
        b[i] = False
    

    for i in range(n):
        n_bois = mat[i][0]
        is_married = 0
        for j in mat[i][1:]:
            if not b[j-1]:
                b[j-1] = True
                is_married = 1
                break
        if is_married == 0:
            not_marrid.append(i)
    
    does_boy_exist = -1
    for i in range(n):
        if not b[i]:
            does_boy_exist = i

    which_girl_left = -1
    if not_marrid != []:
        which_girl_left = not_marrid[0]

    if which_girl_left == -1:
        print("OPTIMAL")
    elif does_boy_exist == -1:
        print("OPTIMAL")
    elif which_girl_left != -1 and does_boy_exist != -1:
        print("IMPROVE")
        print(which_girl_left+1,does_boy_exist+1)
    else:
        print("OPTIMAL")
    


