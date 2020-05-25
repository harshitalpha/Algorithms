# def is_palindrome(arr):
#     n = len(arr)
#     i = 0
#     j = n-1
#     while(i<j):
#         if arr[i] != arr[j]:
#             return 0
#         i = i + 1
#         j = j - 1
#     return 1

t = int(input())
while(t):
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i+2,n):
            if a[j] == x:
                ans = 1
                break
    
    if ans:
        print("YES")
    else:
        print("NO")

