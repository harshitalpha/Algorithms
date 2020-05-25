'''
    Minimum Cost Path
'''
import copy
def solve(mat):
    r = len(mat)
    c = len(mat[0])

    for j in range(1,c):
        for i in range(r):
            if i == 0:
                x = mat[i][j-1]
            else:
                x = min(mat[i][j-1], mat[i-1][j-1],mat[i-1][j])
            mat[i][j] = mat[i][j] + x
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print("\n")
    print(mat[r-1][c-1])
    return mat

def get_path(mat,t_mat):
    r = len(mat) -1
    c = len(mat[0]) -1
 
    path = []
    path.append([r,c])
    while r != 0 and c != 0:
        
        mat_val = mat[r][c]
        t_mat_val = t_mat[r][c]
        next_val = t_mat_val - mat_val
        if t_mat[r-1][c-1] == next_val:
            r = r - 1
            c = c - 1
        elif t_mat[r][c-1] == next_val:
            c = c - 1
        elif t_mat[r-1][c] == next_val:
            r = r - 1
        path.append([r,c])
    path.append([0,0])
    return path
        
 

if __name__ == "__main__":
    mat = [[1,2,3],[4,8,2],[1,5,3]]
    mat1 = copy.deepcopy(mat)
    t_mat = solve(mat1)
    print("PATH")

    path = get_path(mat,t_mat)
    print(path[::-1])
