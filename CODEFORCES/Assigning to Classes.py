t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(s) for s in input().split()]
    arr.sort()
    if n % 2 == 0:
        last = arr[-1]
        sec_last = arr[-2]
        arr = arr[:-2]
        ans1 = []
        ans2 = []
        i = 0
        while i < 2 * (n - 1):
            ans1.append(arr[i])
            ans2.append(arr[i + 1])
            i += 2
        ans1.append(sec_last)
        ans1.append(last)
        m1 = ans1[int((n / 2))]
        m2 = ans2[int((n - 2) / 2)]
        ans_arr = [abs(m1 - m2)]
        ans1 = ans1[:-2]
        ans2.append(sec_last)
        ans2.append(last)
        m1 = ans1[int((n-2) / 2)]
        m2 = ans2[int((n / 2))]
        ans_arr.append(abs(m1 - m2))
        print(min(ans_arr))
    else:
        ans1 = []
        ans2 = []
        i = 0
        while i < 2 * n:
            ans1.append(arr[i])
            ans2.append(arr[i + 1])
            i += 2
        m1 = ans1[int((n - 1) / 2)]
        m2 = ans2[int((n - 1) / 2)]
        ans = abs(m1 - m2)
        print(ans)
