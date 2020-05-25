n, q = [int(s) for s in input().split()]
arr = []
for i in range(q):
    arr.append([int(s) for s in input().split()])

maze = [[0 for i in range(n)] for j in range(2)]
gate_open = True
gate_count = 0
ans = []
for i in range(q):
    tile = arr[i][1]
    level = arr[i][0] - 1
    if maze[level][tile - 1] == 0:
        maze[level][tile-1] = 1
        if maze[0][tile-1] == 1 and maze[1][tile-1] == 1:
            gate_count += 1
        if tile <= n-1:
            if maze[1 - level][tile] == maze[level][tile - 1]:
                gate_count += 1
        if tile - 2 >= 0:
            if maze[1 - level][tile - 2] == maze[level][tile - 1]:
                gate_count += 1
    else:
        if maze[0][tile-1] == 1 and maze[1][tile-1] == 1:
            gate_count -= 1
        if tile <= n-1:
            if maze[1-level][tile] == maze[level][tile-1]:
                gate_count -= 1
        if tile - 2 >= 0:
            if maze[1-level][tile-2] == maze[level][tile-1]:
                gate_count -= 1
        maze[level][tile-1] = 0
    if gate_count > 0:
        gate_open = False
    else:
        gate_open = True
    if gate_open:
        ans.append("yes")
    else:
        ans.append("no")
    # print(maze)
    # print(gate_count)

# print(ans)
for i in ans:
    print(i, end=" ")
print()