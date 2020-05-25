t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(s) for s in input().split()])
    
    is_first_inceasing = 1
    is_second_increasing = 1
    is_sec_grater_one = 1
    flag = 1

    if a[0][0] < a[0][1]:
        is_sec_grater_one = 0

    for i in range(1,n):
        if a[i][0] < a[i-1][0]:
            is_first_inceasing = 0
        if a[i][1] < a[i-1][1]:
            is_second_increasing = 0
        if a[i][0] < a[i][1]:
            is_sec_grater_one = 0
        if a[i][1] > a[i-1][1]:
            no_of_clear_inc = a[i][1] - a[i-1][1]
            no_of_player_inc = a[i][0] - a[i-1][0]
            if no_of_clear_inc > no_of_player_inc:
                flag = 0


    
    if is_first_inceasing and is_sec_grater_one and is_second_increasing and flag:
        print("YES")
    else:
        print("NO")




