t = int(input())
while t:
    t = t - 1
    n, k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    d = {}
    d[0] = 0
    for i in range(1,n-1):
        current_height = a[i]
        if a[i-1] < current_height and a[i+1] < current_height:
            d[i] = d[i-1] + 1
        else:
            d[i] = d[i-1]
    d[n-1] = d[n-2]
    temp_d = d.copy()
    for i in range(1,n):
        if temp_d[i] > d[i-1]:
            temp_d[i] = temp_d[i] - 1
    d = temp_d
    n_range = n - k + 1
    max_peak = 0
    optimal_l = 0
    for i in range(n_range):
        l = i
        r = i+k-1
        n_peaks = d[r]-d[l+1]
        if n_peaks > max_peak:
            max_peak = n_peaks
            optimal_l = l

    print(max_peak+1,optimal_l+1)