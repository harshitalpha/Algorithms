import math
for _ in range(int(input())):
    r, c = [int(s) for s in input().split()]
    if r%2 == 0:
        ans = (r/2)*c
    else:
        ans = (r-1)/2 * c
        ans = ans + math.ceil(c/2)
    print(int(ans))