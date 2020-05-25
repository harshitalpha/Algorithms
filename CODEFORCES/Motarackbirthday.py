def all_minus(arr):
    for i in arr:
        if i != -1:
            return 0
    return 1
t = int(input())
while t:
    t=t-1
    n = int(input())
    arr = [int(s) for s in input().split()]
    # if all_minus(arr):
    #     print("0 0")
    # else:
    #     if arr[0] == -1:
    #         flagr = 1
    #     else:
    #         flagr = 0
    #     if arr[n-1] == -1:
    #         flagl = 1
    #     else:
    #         flagl = 0
    #     # print(flagr, flagl)
    #     index_arr = []
    #     for i in range(n):
    #         if arr[i] != -1:
    #             index_arr.append(i)
    #     # print(index_arr)
    #     sub_arr = []
    #     for i in range(len(index_arr)-1):
    #         cur_id = index_arr[i]
    #         next_id = index_arr[i+1]
    #         if next_id != cur_id+1:
    #             sub_arr.append(int((arr[cur_id] + arr[next_id])/2))
    #     # print(sub_arr)
    #     if len(sub_arr) != 0:
    #         ans = max(sub_arr)
    #     else:
    #         if flagl and flagr:
    #             for i in range(n):
    #                 if arr[i] != -1:
    #                     p1 = arr[i]
    #                     break
    #             for i in range(n-1,-1,-1):
    #                 if arr[i] != -1:
    #                     p2 = arr[i]
    #                     break
    #             # print(p1, p2)
    #             ans = int((p1 + p2)/2)
    #         elif flagr:
    #             for i in range(n):
    #                 if arr[i] != -1:
    #                     p1 = arr[i]
    #                     break
    #             ans = p1
    #         elif flagl:
    #             for i in range(n-1,-1,-1):
    #                 if arr[i] != -1:
    #                     p2 = arr[i]
    #                     break
    #             ans = p2
    #
    #     for i in range(n):
    #         if arr[i] == -1:
    #             arr[i] = ans
    #
    #     diff = 0
    #     for i in range(n-1):
    #         if abs(arr[i] - arr[i+1]) > diff:
    #             diff = abs(arr[i] - arr[i+1])
    #     print(diff, end=" ")
    #     print(ans)
    if all_minus(arr):
        print("0 0")
    else:
        all_pos = []
        for i in arr:
            if i > 0:
                all_pos.append(i)
        if len(all_pos) > 0:
            ans = int(sum(all_pos)/len(all_pos))
            for i in range(n):
                if arr[i] == -1:
                    arr[i] = ans
            diff = 0
            for i in range(n - 1):
                if abs(arr[i] - arr[i + 1]) > diff:
                    diff = abs(arr[i] - arr[i + 1])
            print(diff, end=" ")
            print(ans)
        else:
            print("0 0")