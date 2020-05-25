n = int(input())

a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]

c = []
for i in range(n):
    c.append(a[i] - b[i])

c.sort()
i = 0
j = n-1

count = 0
while(i < j):
    if c[i] > 0:
        count = count + (j-i)
        j = j - 1
        continue
    elif abs(c[i]) < c[j]:
        count = count + (j-i)
        j = j - 1
    else:
        i = i + 1
print(count)