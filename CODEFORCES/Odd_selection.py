t = int(input())
while t:
    t -= 1
    n, x = [int(s) for s in input().split()]
    arr = [int(s) for s in input().split()]
    count_odd = 0
    count_even = 0
    for i in arr:
        if i%2 == 0:
            count_even += 1
        else:
            count_odd += 1

    if count_odd == 0:
        ans = False
    else:
        if count_odd%2 != 0:
            if count_odd >= x:
                ans = True
            else:
                remaining_x = x - count_odd
                if remaining_x <= count_even:
                    ans = True
                else:
                    ans = False
        else:
            count_odd = count_odd - 1
            if count_odd >= x:
                ans = True
            else:
                remaining_x = x - count_odd
                if remaining_x <= count_even:
                    ans = True
                else:
                    ans = False

    if ans:
        print("Yes")
    else:
        print("No")