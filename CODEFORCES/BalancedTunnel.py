n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
visit = {}
for i in a:
    visit[i] = 0
i = 0
j = 0
fine = []
while(i < n):
    if not visit[a[i]]:
        #print(a[i])
        #print(i,j)
        while(j < n):
            #print(j, b[j])
            if b[j] == a[i]:
                visit[a[i]] = 1
                j=j+1
                break
            else:
                visit[b[j]] = 1
                fine.append(b[j])
                j=j+1
        #print(i, j)
    i += 1
#print(fine)
print(len(fine))

