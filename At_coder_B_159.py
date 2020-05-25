def compute_fact(n):
    global f
    if(n < 2):
        f = [1,1]
    else:
        f = [0 for i in range(n+1)]
        f[0] = 1
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1]*i

def compute_c(n,r):
    compute_fact(n)
    ans = f[n]/(f[r] * f[n-r])
    return ans

n,m = [int(s) for s in input().split()]
if n >= 2 and m >= 2:
    print(int(compute_c(n,2) + compute_c(m,2)))
elif n >= 2:
    print(int(compute_c(n,2)))
elif m >= 2:
    print(int(compute_c(m,2)))
else:
    print(0)
    