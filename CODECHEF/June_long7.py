t = int(input())
while t:
    t -= 1
    inp = [int(s) for s in input().split()]
    out = [int(s) for s in input().split()]
    diff = []
    div = []
    for i in range(3):
        if out[i] - inp[i] > 0:
            diff.append(out[i] - inp[i])
        if out[i] / inp[i] > 1:
            div.append(out[i] / inp[i])

