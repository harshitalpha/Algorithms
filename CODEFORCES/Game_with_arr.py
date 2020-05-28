n, s = [int(s) for s in input().split()]
if s-n < n:
    print("NO")
else:
    first_element = s - (n - 1)
    if (n-1) + 1 == first_element:
        print("NO")
    else:
        print("YES")
        print(first_element, end=" ")
        for i in range(n-1):
            print("1", end=" ")
        print()
        print(n)