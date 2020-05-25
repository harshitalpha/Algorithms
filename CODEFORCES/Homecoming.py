t = int(input())
while(t):
    t=t-1
    a,b,p = [int(s) for s in input().split()]
    s = [i for i in input()]
    n = len(s)
    payable_station_name = []
    payable_station_id = []
    cost_has_to_paid = []
    x = s[n-2]
    payable_station_name.append(s[n-1])
    payable_station_id.append(n-1)
    for i in range(n-2,-1,-1):
        if s[i] != x:
            payable_station_name.append(x)
            payable_station_id.append(i+1)
            x = s[i]
    
    payable_station_id.append(0)
    payable_station_name.append(s[0])

    # print(payable_station_name)
    # print(payable_station_id) 
    station_at_which_reach = 0
    for i in range(1,len(payable_station_name)):
        station = payable_station_name[i]
        if station == "A":
            if p >= a:
                p = p - a
            else:
                station_at_which_reach = payable_station_id[i-1]
                break
        elif station == "B":
            if p >= b:
                p = p - b
            else:
                station_at_which_reach = payable_station_id[i-1]
                break
    print(station_at_which_reach+1)
        