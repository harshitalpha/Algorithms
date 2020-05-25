import math


def return_needed_power(monster_power, a, b):
    if monster_power <= a:
        return 0
    elif monster_power <= a + b:
        ans = math.ceil(monster_power / a) - 1
        return ans
    else:
        remaining_power = monster_power % (a + b)
        if remaining_power == 0:
            ans = math.ceil((a + b) / a) - 1
            return ans
        else:
            if remaining_power <= a:
                return 0
            elif remaining_power <= a + b:
                ans = math.ceil(remaining_power / a) - 1
                return ans


n, a, b, k = [int(s) for s in input().split()]
arr = [int(s) for s in input().split()]
power_arr = []
for i in arr:
    power_arr.append(return_needed_power(i, a, b))
# print(power_arr)
power_arr.sort()
# print(power_arr)
count = 0
# print(k)
for i in power_arr:
    # print(i)
    if i <= k:
        # print(k)
        # print(count)
        count = count + 1
        k = k - i
        # print(k)
        # print(count)
print(count)
