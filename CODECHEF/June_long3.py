for _ in range(int(input())):
    n = int(input())
    arr = [int(s) for s in input().split()]
    coin5 = 0
    coin10 = 0
    coin15 = 0
    ans = True
    for i in arr:
        if i == 5:
            coin5 = coin5 + 1
        elif i == 10:
            change = 5
            if coin5 >= 1:
                coin5 = coin5 - 1
                coin10 = coin10 + 1
            else:
                ans = False
                break
        else:
            change = 10
            if coin10 >= 1:
                coin10 = coin10 - 1
                coin15 = coin15 + 1
            elif coin5 >= 2:
                coin5 = coin5 - 2
                coin15 = coin15 + 1
            else:
                ans = False
                break
    if ans:
        print("YES")
    else:
        print("NO")