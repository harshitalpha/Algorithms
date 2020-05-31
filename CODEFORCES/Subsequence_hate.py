t = int(input())
while t:
    t -= 1
    str = [int(s) for s in input()]
    if str[0] == 0:
        number = [0]
        count = [1]
    if str[0] == 1:
        number = [1]
        count = [1]
    count0 = 0
    count1 = 0
    for i in str:
        if i == 1:
            count1 += 1
        else:
            count0 += 1

    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            count[-1] = count[-1] + 1
        else:
            number.append(str[i])
            count.append(1)

    # zero_left = []
    # one_left = []
    # zero_right = []
    # one_right = []
    #
    # for i in range(len(number)):


    dp = []
    for i in range(len(number)):
        cur_count = 0
        for j in range(i, len(number)):
            if number[j] == 0:
                cur_count = cur_count + count[j]
        for k in range(0, i):
            if number[k] == 1:
                cur_count = cur_count + count[k]
        dp.append(cur_count)

    dp_1 = []
    for i in range(len(number)):
        cur_count = 0
        for j in range(i, len(number)):
            if number[j] == 1:
                cur_count = cur_count + count[j]
        for k in range(0, i):
            if number[k] == 0:
                cur_count = cur_count + count[k]
        dp_1.append(cur_count)

    # print(number)
    # print(count)
    # print(dp)
    # print(dp_1)
    print(min(min(dp), min(dp_1)))