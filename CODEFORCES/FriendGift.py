n = int(input())
arr = [int(s) for s in input().split()]
recieved = [0 for i in range(n+1)]
# given = [0 for i in range(n+1)]
for i in range(n):
    recieved[arr[i]] = 1
given = arr.copy()
given.insert(0,0)
left_recieved = []
left_given = []

for i in range(1, n+1):
    if recieved[i] == 0:
        left_recieved.append(i)
    if given[i] == 0:
        left_given.append(i)


#
# print(left_recieved)
# print(left_given)

problem = []
l = len(left_recieved)
for i in range(l):
    if left_recieved[i] == left_given[i]:
        problem.append([left_recieved[i], left_given[i]])


# print(problem)
# print(len(problem))
# l = len(left_recieved)
if len(problem) == 1:
    for i in range(l):
        # print("Hello")
        if left_given[i] != left_recieved[i]:
            problem.append([left_recieved.pop(i), left_given.pop(i)])
            break

# print(problem)
#
# print(left_recieved)
# print(left_given)
d = {}
l = len(left_recieved)
for i in range(l):
    if left_given[i] != left_recieved[i]:
        d[left_given[i]] = left_recieved[i]

# print(d)
l = len(problem)
# print(l)
if l != 0:
    for i in range(l-1):
        d[problem[i][1]] = problem[i+1][0]

    d[problem[l-1][1]] = problem[0][0]

# print(d)
ans = []
for i in range(n):
    if arr[i] != 0:
        ans.append(arr[i])
    else:
        ans.append(d[i+1])

for i in ans:
    print(i, end=" ")
print()