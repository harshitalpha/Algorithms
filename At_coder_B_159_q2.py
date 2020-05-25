def is_palindrome(s):
    i = 0
    j = len(s)-1
    flag = 1
    while(i<j):
        if s[i] != s[j]:
            flag = 0
            break
        i = i + 1
        j = j - 1
    return(flag)

s = input()
n = len(s)
f1 = int(((n+1)/2) - 1)
f2 = int((n+3)/2 - 1)

if is_palindrome(s) and is_palindrome(s[:f1]) and is_palindrome(s[f2:]):
    print("Yes")
else:
    print("No")