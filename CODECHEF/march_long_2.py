def is_odd_or_even_ones(n):
    c = 0
    while(n):
        x = n%2
        if(x == 1):
            c = c + 1
        n = n/2
    if(c%2 == 0):
        return 1
    else:
        return 0


def flip_or_not(eve_count, odd_count, px):
    if(px == 1):
        return eve_count,odd_count
    else:
        return odd_count,eve_count

t = int(input())

n, q = [int(x) for x in input().split()]

arr = [unsigned long(int(s)) for s in input().split()]

odd_count = 0
eve_count = 0

for i in arr:
    x = is_odd_or_even_ones(i)
    if(x == 1):
        eve_count += 1
    else:
        odd_count += 1

print("Eve = {}".format(eve_count))
print("odd = {}".format(odd_count))


'''
while(q):
    q = q - 1
    p = int(input())

    px = is_odd_or_even_ones(p)

    eve_count, odd_count = flip_or_not(eve_count,odd_count,px)

print(eve_count, end = " ")
print(odd_count)
'''
