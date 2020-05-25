t = int(input())
while(t):
    t = t -1
    l,r,d,u = [int(s) for s in input().split()]
    x,y,x1,y1,x2,y2 = [int(s) for s in input().split()]

    final_x = x - l + r
    final_y = y - d + u

    ans = 1
    if final_x < x1 or final_x > x2:
        ans = 0
    if final_y < y1 or final_y > y2:
        ans = 0
    
    if x == x1 == x2 and y == y1 == y2 and (l > 0 or r > 0 or d > 0 or u >0):
        ans = 0

    if y == y1 == y2 and (u > 0 or d > 0):
        ans = 0
    
    if x == x2 == x1 and (r > 0 or l > 0):
        ans = 0

    if ans:
        print("Yes")
    else:
        print("No")


