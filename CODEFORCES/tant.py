from sys import stdin, stdout
n, sx, sy = [int(s) for s in stdin.readline().split()]
points = []
for i in range(n):
    points.append([int(s) for s in stdin.readline().split()])
for i in range(n):
    points[i][0] = points[i][0] - sx
    points[i][1] = points[i][1] - sy

right = 0
left = 0
up = 0
down = 0
for i in range(n):
    x = points[i][0]
    y = points[i][1]
    if x > 0:
        right = right + 1
    if y > 0:
        up = up + 1
    if x < 0:
        left = left + 1
    if y < 0:
        down = down + 1

no_of_student = max(right, left, up, down)
if right == no_of_student:
    ans_x = sx + 1
    ans_y = sy
elif left == no_of_student:
    ans_x = sx - 1
    ans_y = sy
elif up == no_of_student:
    ans_x = sx
    ans_y = sy + 1
else:
    ans_x = sx
    ans_y = sy - 1

# print(right, left, up, down)
stdout.write("{}\n".format(no_of_student))
stdout.write("{} {}".format(ans_x, ans_y))
