t = int(input())

while(t):
    t = t - 1
    n = int(input())
    
    arr = [int(s) for s in input().split()]
    
    arr.sort()
    
    a = []
    
    i = 0
    j = n-1
    
    while(i <= j):
        if(i != j):
            a.append(arr[i])
            a.append(arr[j])
        else:
            a.append(arr[i])
        i = i + 1
        j = j - 1
    
    s = 0
    for i in range(len(a)-1):
        s = s + abs(a[i] - a[i+1])
    
    s = s + abs(a[0] - a[n-1])
    
    print(s)
