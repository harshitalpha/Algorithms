def solve(start, end):
    index = list(range(len(end)))
    
    index.sort(key = lambda i:end[i])
    
    out = []
    
    curr_end_time = 0
    
    
    for i in index:
        if start[i] >= curr_end_time:
            out.append(i+1)
            curr_end_time = end[i]
    
    return out
            
def main():
    
    t = int(input("Enter Test Cases "))
    
    while(t):
        t = t - 1
        n = int(input("Enter the size of array"))
        
        print("Enter Arrays Start and End")
        
        start = [int(s) for s in input().split()]
        end = [int(s) for s in input().split()]
        
        ans = solve(start,end)
        
        
        print("Maximum following Meeting can be conducted in room")
        for i in range(len(ans)):
            if i != len(ans) - 1:
                print(ans[i], end = " ")
            else:
                print(ans[i])
            
        
        
        
if __name__ == "__main__":
    main()
            
