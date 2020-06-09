def solve(arr, swaps):
    if swaps == 0 or arr == []:
        return arr
    if len(arr) == 1:
        return arr
    else:
        min_index = arr.index(min(arr[1:1+swaps]))
        element = arr[min_index]
        if arr[0] < element:
            return [arr[0]] + solve(arr[1:], swaps)
        swaps = swaps - min_index
        element = arr.pop(min_index)
        new_arr = [element] + arr
        return new_arr[:min_index] + solve(new_arr[min_index:], swaps)

t=int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    ansArr = solve(arr, n-1)
    print(*ansArr)