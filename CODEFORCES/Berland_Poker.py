import math
t = int(input())
while t:
    t = t - 1
    n, m, k = [int(s) for s in input().split()]
    if m == 0:
        print("0")
    elif n == m:
        print("0")
    else:
        if n/k >= m:
            print(m)
        else:
            jocker_left = m - (n/k)
            player_left = k - 1
            distributed_cards = math.ceil(jocker_left / player_left)
            print(int(n/k)-distributed_cards)