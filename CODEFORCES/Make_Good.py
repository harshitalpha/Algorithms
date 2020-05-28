t = int(input())
while t:
    t = t - 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    S = sum(arr)
    if n >= 2:
        X = arr[0] ^ arr[1]
        for i in range(2,n):
            X = X ^ arr[i]
    else:
        X = arr[0]
    print("2")
    print(S+X, X)