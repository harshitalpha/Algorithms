def solve(arr, s, x, subP):
    print(arr)
    print(s)
    if arr == []:
        if s%x == 0:
            print(-1)
            return -1
        else:
            if subP == 1:
                print(0)
                return 0
            else:
                print(0)
                return 0
    else:
        a = solve(arr[1:], s+arr[0], x, 0)
        b = solve(arr[1:], s, x, 1)
        if subP != 2:
            if a != -1:
                a = a + 1
        print(f"a : {a}")
        print(f"b : {b}")
        print(max(a,b))
        return max(a,b)

t = int(input())
while t:
    t -= 1
    n, x = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    print(solve(a, 0, x, 2))