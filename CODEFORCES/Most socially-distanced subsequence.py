t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    intact = [arr[0]]
    for i in range(1, n-1):
        x = abs(arr[i]-intact[-1]) + abs(arr[i] - arr[i+1])
        y = abs(intact[-1]-arr[i+1])
        if y < x:
            intact.append(arr[i])
    intact.append(arr[n-1])
    print(len(intact))
    print(*intact)
