for _ in range(int(input())):
    n = int(input())
    arr = [int(s) for s in input().split()]
    arr.sort()
    count = 0
    mask = [i+1 for i in range(n)]
    # print(mask)
    for i in range(n-1,-1,-1):
        if mask[i] >= arr[i]:
            count = mask[i]
            break
    print(count+1)