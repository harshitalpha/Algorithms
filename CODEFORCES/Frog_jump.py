t = int(input())
while(t):
    t = t - 1
    st = [s for s in input()]
    st.append("F")
    st.insert(0,'R')
    is_r = -1
    n = len(st)
    x = []
    last = n-1
    for i in range(n-1,-1,-1):
        if st[i] == 'R':
            x.append(last - i)
            last = i
    print(max(x))