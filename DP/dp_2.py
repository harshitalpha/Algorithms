'''
    SUBSET SUM PROBLEM : 
        If the given sum can be made from subset of given set with some element.
        Eg : {3,4,5,2} , sum = 9
            Ans = True 
            since 9 can be made from {4,5} or {3,4,2}
'''
def solve(arr,s):

    mat = [[None for i in range (s+1)] for j in range(len(arr) + 1)]

    for i in range(len(arr)+1):
        mat[i][0] = True
    
    for j in range(1,s+1):
        mat[0][j] = False

    for i in range(1,len(arr) + 1):
        for j in range(1,s+1):
            if j < arr[i-1]:
                mat[i][j] = mat[i-1][j]
            elif j == arr[i-1]:
                mat[i][j] = True
            else:
                mat[i][j] = mat[i-1][j] or mat[i-1][j-arr[i-1]]
    
    for i in range(len(arr)+1):
        for j in range(s+1):
            print(mat[i][j] ,end=" ")
        print("\n")
    
    return mat[len(arr)][s]


if __name__ =="__main__":
    arr = [3,4,5,2]
    s = 15

    print(solve(arr, s))
