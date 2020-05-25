t = int(input())
while(t):
    t = t -1
    a,b  = [int(s) for s in input().split()]

    t_a = int(a/10)
    o_a = a - (int(a/10) * 10)
    t_b = int(b/10)
    o_b = b - (int(b/10) * 10)

    d1 = t_a * 10 + o_b
    d2 = t_b * 10 + o_a

    print(a)
    print(b)
    print(d1)
    print(d2)

    a = [a,b,d1,d2]

 