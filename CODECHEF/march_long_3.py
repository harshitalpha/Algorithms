def is_safe(x,y):
	return (x>=0 and x<=7 and y>=0 and y<=7)

def is_fill(x,y,moves):
    return moves[x][y]


t = int(input())

while(t):
    moves=[[0 for i in range(8)] for j in range(8)]

    seq_of_moves = []

    count=-1
    visited_count = 0

    xx=[1,1,-1,-1]
    yy=[-1,1,1,-1]

    xxx=[-1,1,1,-1]
    yyy=[-1,1,-1,1]

    xq = []
    yq = []

    t = t - 1
    x,y = [int(s) for s in input().split()]
    x = x -1
    y = y -1

    xq.append(x)
    yq.append(y)

    while(len(xq) > 0 and visited_count < 32):
        cur_x = xq.pop(0)
        cur_y = yq.pop(0)
        if moves[cur_x][cur_y] == 0:
            moves[cur_x][cur_y] = 1
            visited_count+=1
        
        count+=1
        seq_of_moves.append([cur_x,cur_y])

        flag = 0
        for i in range(4):
            after_move_x = cur_x + xx[i]
            after_move_y = cur_y + yy[i]

            if is_safe(after_move_x,after_move_y) and (not is_fill(after_move_x, after_move_y,moves)):
                xq.append(after_move_x)
                yq.append(after_move_y)
                flag = 1
                break
        
        if(flag == 0):
            for i in range(4):
                after_move_x = cur_x + xxx[i]
                after_move_y = cur_y + yyy[i]

                if is_safe(after_move_x,after_move_y):
                    xq.append(after_move_x)
                    yq.append(after_move_y)
                    break
    print(count)
    for i in range(1,len(seq_of_moves)):
        print(seq_of_moves[i][0], end = " ")
        print(seq_of_moves[i][1])
            

                

            








