from sys import stdin, stdout
t = int(input())
while t:
    t = t - 1
    n = int(stdin.readline())
    if n == 1:
        _ = stdin.readline()
        stdout.write("YES\n")
    else:
        p = [int(s) for s in stdin.readline().split()]
        id = [0 for i in range(n)]
        for i in range(n):
            id[p[i]-1] = i
        # print(id)
        for i in range(n):
            id[i] = id[i] - i
        ans = 1
        # print(id)
        for i in range(1,n):
            if id[i] > id[i-1]:
                ans = 0
        if ans:
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")