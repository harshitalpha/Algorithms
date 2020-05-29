import itertools

n = int(input())
arr = [int(s) for s in input().split()]
cur_sum = 0
visited_emp = {}
ans_arr = [-1]
ans = 1
for i in range(n):
    if arr[i] > 0:
        try:
            x = visited_emp[arr[i]]
            if cur_sum == 0:
                ans_arr.append(i-1)
                visited_emp = {}
            else:
                ans = -1
                break
        except KeyError:
            cur_sum = cur_sum + arr[i]
            visited_emp[arr[i]] = 1
    if arr[i] < 0:
        try:
            x = visited_emp[abs(arr[i])]
            if x == 1:
                cur_sum = cur_sum + arr[i]
        except KeyError:
            ans = -1
            break
    if cur_sum == 0:
        ans_arr.append(i)
        visited_emp = {}
    # print(cur_sum)
# print(ans)
# print(ans_arr)
if cur_sum != 0:
    ans = -1

if ans == -1:
    print(ans)
else:
    final_ans = []
    for i in range(1, len(ans_arr)):
        final_ans.append(ans_arr[i] - ans_arr[i-1])
    print(len(final_ans))
    print(*final_ans)