t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    a.sort(reverse= True)
    for i in a:
        print(i,end = " ")
    print()