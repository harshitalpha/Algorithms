'''
    Gold Mine Problem 
'''
def solve(mat):
    r = len(mat)
    c = len(mat[0])

    for j in range(1,c):
        for i in range(r):
            if i == 0:
                x = max(mat[i+1][j-1],mat[i][j-1])
            elif i == r-1:
                x = max(mat[i-1][j-1],mat[i][j-1])
            else:
                x = max(mat[i][j-1], mat[i+1][j-1], mat[i-1][j-1])
            mat[i][j] = mat[i][j] + x
    # finding the answer 
    # finding the maximum of last column
    ans = 0
    for i in range(r):
        if(mat[i][c-1] > ans):
            ans = mat[i][c-1]

    # printing the transformed matrix
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print("\n")
    
    print(ans)

if __name__ == "__main__":
    mat = [[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]
    solve(mat)
