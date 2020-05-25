def fun(a):
    if a < 9:
        return a + 1
    else:
        return a - 1

t = int(input())

while(t):
    t = t - 1
    suduko = []
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])
    suduko.append([w for w in input()])

    suduko[0][0] = str(fun(int(suduko[0][0])))
    suduko[1][3] = str(fun(int(suduko[1][3])))
    suduko[2][6] = str(fun(int(suduko[2][6])))
    suduko[3][1] = str(fun(int(suduko[3][1])))
    suduko[4][4] = str(fun(int(suduko[4][4])))
    suduko[5][7] = str(fun(int(suduko[5][7])))
    suduko[6][2] = str(fun(int(suduko[6][2])))
    suduko[7][5] = str(fun(int(suduko[7][5])))
    suduko[8][8] = str(fun(int(suduko[8][8])))

    for i in range(9):
        for j in range(9):
            print(suduko[i][j],end="")
        print()

