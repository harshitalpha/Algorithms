import math
t = int(input())
while t:
    t = t - 1
    n, g, b = [int(s) for s in input().split()]
    good_days = math.ceil(n/2)
    no_matter_days = n - good_days

    good_set = int(good_days / g)
    remaining_good_days = int(good_days % g)


    if remaining_good_days == 0:
        bad_set = good_set - 1
        required_days = (good_set * g) + (bad_set * b)
        bad_days = bad_set * b
        if bad_days >= no_matter_days:
            ans = required_days
        else:
            remaining_bed_days = no_matter_days - bad_days
            ans = required_days + remaining_bed_days
    else:
        bad_set = good_set
        required_days = (good_set * g) + (bad_set * b)
        bad_days = bad_set * b
        if bad_days >= no_matter_days:
            ans = required_days + remaining_good_days
        else:
            remaining_bed_days = no_matter_days - bad_days
            ans = required_days + remaining_bed_days + remaining_good_days

    print(ans)
