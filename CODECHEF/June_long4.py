import math
for _ in range(int(input())):
    n = int(input())
    if n % 2 != 0:
        ans = int((n / 2))
        print(ans)
    else:
        if math.ceil(math.log2(n)) == math.floor(math.log2(n)):
            print(0)
        else:
            x = n
            count = 1
            while(1):
                if x%2==1:
                    break
                else:
                    x = x / 2
                    count += 1
            start = 2 ** (count)
            print(int(n / start))
