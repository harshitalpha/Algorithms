def solve(arr, swaps):
    if swaps <= 0 or arr == [] or len(arr) == 1:
        return arr
    else:
        first0 = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                first0 = i
                break
        if first0 == -1:
            return arr
        swap_with = first0 - swaps if first0 - swaps > 0 else 0
        swaps = swaps - first0
        arr[first0] = 1
        arr[swap_with] = 0
        # print(first0)
        # print(arr)
        # print(swaps)
        return arr[:swap_with+1] + solve(arr[swap_with+1:], swaps)


t = int(input())
while t:
    t -= 1
    n, k = [int(s) for s in input().split()]
    arr = [int(s) for s in input()]
    ans = solve(arr, k)
    for i in ans:
        print(i, end="")
    print()
