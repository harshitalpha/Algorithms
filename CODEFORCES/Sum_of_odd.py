t = int(input())
while(t):
    t = t -1
    n,k = [int(s) for s in input().split()]
    if n%2 == 0 and k%2 == 0:
        print("YES")
    elif n%2 == 0 and k%2 != 0:
        print("NO")
    elif n%2 != 0 and k%2 != 0:
        print("YES")
    else:
        print("NO")