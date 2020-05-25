'''
Friends Pairing Problem 

Given n friends,
each one can remain single or can be paired up with some other friend. 
Each friend can be paired only once. 
Find out the total number of ways in which friends can remain single or can be paired up.
'''

'''
    Approch is :
        F(n) = ways n people can remain single or pair up.
        For n-th person there are two choices:
            1) n-th person remains single, we recurse for f(n - 1)
            2) n-th person pairs up with any of the remaining n - 1 persons. 
                We get (n - 1) * f(n - 2)
    f(n) = f(n - 1) + (n - 1) * f(n - 2)
'''
F = {}

def find_total_pair(n):
    if(n <= 1):
        return 1
    else:
        if(n in F.keys()):
            return F[n]
        else:
            F[n] = find_total_pair(n-1) + (n-1) * find_total_pair(n-2)
            return F[n]

if __name__ == "__main__":
    ans = find_total_pair(6)
    print(ans)
