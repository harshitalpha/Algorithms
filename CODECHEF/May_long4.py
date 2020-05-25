import math
def countBits(number):
    return int((math.log(number) / math.log(2)) + 1)

t = int(input())
while t:
    t = t - 1
    x, y, l, r = [int(s) for s in input().split()]
    if x == 0 or y == 0:
        print(0)
    else:
        z = x|y
        if z <= r:
            print(z)
        else:
            try:
                no_bit_x = countBits(x)
                no_bit_y = countBits(y)
                no_bit_z = countBits(z)
                no_bit_r = countBits(r)
                # print(no_bit_r)
                # print(no_bit_y)
                # print(no_bit_x)
                # print(no_bit_z)
                # print(z)
                # print(r)
                if min(no_bit_x, no_bit_y) >= no_bit_r:
                    # print("Hello")
                    ans = z&r
                    # print(ans)
                else:
                    u = min(x, y)
                    no = 2 ** countBits(u) - 1
                    # print(u)
                    # print(no)
                    ans = (z&no)|u
                print(ans)
            except Exception:
                pass


