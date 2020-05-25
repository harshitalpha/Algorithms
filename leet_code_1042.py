import Graph as g

def solve(n,path):
    flower = [[1,2,3,4] for i in range(n)]
    graph = g.Graph(vertices=n)
    for a,b in path:
        graph.add_edge(a-1,b-1)
    
    d = graph.Adj_list

    done = []
    for i in range(n):
        for j in d[i]:
            if j not in done:
                if flower[i][0] in flower[j]:
                    flower[j].remove(flower[i][0])
                if flower[j][0] in flower[i]:
                    flower[i].remove(flower[j][0])
        done.append(i)
    ans = []
    for i in range(n):
        ans.append(flower[i][0])

    return ans


'''
    You have N gardens, labelled 1 to N.  
    In each garden, you want to plant one of 4 types of flowers.

    paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

    Also, there is no garden that has more than 3 paths coming into or leaving it.

    Your task is to choose a flower type for each garden such that, 
    for any two gardens connected by a path, they have different types of flowers.

    Return any such a choice as an array answer, 
    where answer[i] is the type of flower planted in the (i+1)-th garden. 
    The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
'''


if __name__ == "__main__":
    n = 6
    path = [[1,2],[3,4],[1,3],[1,4],[3,6],[4,5]]

    ans = solve(n,path)

    print(ans)




    