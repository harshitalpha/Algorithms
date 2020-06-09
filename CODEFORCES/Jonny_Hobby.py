def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def Count_no_one(arr):
    c = 0
    for i in arr:
        if i == 1:
            c += 1
    return c

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    s = set(arr)
    flag = 1
    for i in range(1, 1024):
        n_set = set([i^j for j in arr])
        if n_set == s:
            print(i)
            flag = 0
            break
    if flag:
        print(-1)