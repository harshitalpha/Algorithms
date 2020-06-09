def decimal_to_binary(n):
    return [int(s) for s in bin(n).replace("0b", "")]

def Count_no_one(arr):
    c = 0
    for i in arr:
        if i == 1:
            c += 1
    return c

t = int(input())
while t:
    t -= 1
    a, b = [int(s) for s in input().split()]
    binA = decimal_to_binary(a)
    binB = decimal_to_binary(b)
    # print(binA)
    # print(binB)
    count_one_a = Count_no_one(binA)
    count_one_b = Count_no_one(binB)
    # print(count_one_a)
    # print(count_one_b)
    if a == b:
        print(0)
    elif count_one_a != count_one_b:
        print(-1)
    else:
        if a < b:
            if binA == binB[:len(binA)]:
                remaining_zero = len(binB) - len(binA)
                ans = int(remaining_zero/3)
                if remaining_zero%3 != 0:
                   ans = ans + 1
                print(ans)
            else:
                print(-1)
        else:
            if binB == binA[:len(binB)]:
                remaining_zero = len(binA) - len(binB)
                ans = int(remaining_zero / 3)
                if remaining_zero % 3 != 0:
                    ans = ans + 1
                print(ans)
            else:
                print(-1)
