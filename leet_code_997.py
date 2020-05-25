import Graph as g

'''
    In a town, there are N people labelled from 1 to N.  
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:
        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
            There is exactly one person that satisfies properties 1 and 2.

    You are given trust, an array of pairs trust[i] = [a, b] 
    representing that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, 
    return the label of the town judge.  Otherwise, return -1.
'''

if __name__ == "__main__":
    n = int(input("Enter No. of vertices"))
    e = int(input("Enter No. of Edges"))
    trust = []
    graph = g.Graph(vertices = n, typeOfGraph = 'directed')
    for i in range(e):
        trust.append([int(s) for s in input().split()])
        graph.add_edge(trust[i][0]-1, trust[i][1]-1)
    
    graph.print_graph()
    
    king = -1
    in_d = 0
    for i in range(n):
        _,in_d = graph.get_degree(i)
        if( in_d == n-1):
            king = i+1
            break
    
    print(king)

    