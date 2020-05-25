
def solve(n,m,f,p):
    d = {}

    for i in range(len(f)):
        if f[i] in d.keys():
            d[f[i]] = d[f[i]] + p[i]
        else:
            d[f[i]] = p[i] 
    
    return d


def main():
    t = int(input())
    while(t):
        t = t - 1
        n, m = [int(x) for x in input().split()]
        f = [int(s) for s in input().split()]
        p = [int(s) for s in input().split()]
        ans = solve(n,m,f,p)
        m = 50 * n
        for i in ans:
            if(ans[i] < m):
                m = ans[i]
        
        print(m, end = " ")

            
    
if __name__ == "__main__":
    main()


