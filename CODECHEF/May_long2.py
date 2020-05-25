t = int(input())
while t:
    t = t - 1
    n, q = [int(s) for s in input().split()]
    s = [s for s in input()]
    dictionary = {}
    for i in s:
        try:
            dictionary[i] = dictionary[i] + 1
        except KeyError:
            dictionary[i] = 1

    while q:
        q = q - 1
        d = dictionary.copy()
        c = int(input())
        for i in d.keys():
            d[i] = d[i] - c if d[i]-c > 0 else 0
        ans = 0
        for i in d.keys():
            ans = ans + d[i]
        print(ans)