'''
    Catalan No.
    c(0) = 1
    c(n+1) = sum(c(i)c(n-i)) for i from 0 to n

    c(n) = 1/(n+1) * (2n-C-n)
    
    c0 = 1
    c1 = 1
    c2 = 2
    c3 = 5
    c4 = 14
    c5 = 42
    c6 = 132
    c7 = 429
    .
    .
    .

    Application : 
        1. No. of expression containing n pair of paranthesis 
            For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
        2. Number of ways a convex polygon of n+2 sides can split into triangles 
            by connecting vertices.
        etc.

        see : https://www.geeksforgeeks.org/applications-of-catalan-numbers/
'''



def solve(n):

    if n == 0 or n == 1:
        return 1

    c = [0 for i in range(n+1)]

    c[0] = 1
    c[1] = 1

    for i in range(2,n+1):
        c[i] = 0
        for j in range(i):
            c[i] = c[i] + c[j] * c[i-j-1]

    return c[n]

n = 4
print(solve(n))    
