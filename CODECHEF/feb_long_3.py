def map_x(x):
    if x == 'A':
        return 0
    elif x== 'B':
        return 1
    elif x == 'C':
        return 2
    else:
        return 3

def map_y(y):
    return int((y/3) - 1)

def find_max_x_y(mat):
    x = 0
    y = 0
    max_val = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] > max_val:
                x = i
                y = j 
                max_val = mat[i][j]
    return x,y,max_val

def del_max_row_col(mat,x,y):
    for i in range(4):
        mat[x][i] = -1
    for i in range(4):
        mat[i][y] = -1

t = int(input())
profit_t = []
while(t):
    t = t - 1
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    n = int(input())
    while(n):
        n = n - 1
        x,y = [s for s in input().split()]
        y = int(y)
        x = map_x(x)
        y = map_y(y)
        mat[x][y] = mat[x][y] + 1

    
    profit = 0

    assigned_solt = [0,0,0,0]

    cost = [100,75,50,25]



    for i in range(4):
        max_x,max_y,val = find_max_x_y(mat)
        if val == 0:
            break
        assigned_solt[max_y] = chr(65+max_x)
        profit = profit + (val * cost[i])
        del_max_row_col(mat,max_x,max_y)
    
    if i != 3:
        deduction = 100 * (4-i)
        profit = profit - deduction

    profit_t.append(profit)
    print(profit)


print(sum(profit_t))






    

