'''
    Largest Sum Contiguos Subarray
    'Kadane's Algorthm'
'''
def find_sum(arr):
    max_so_far = 0
    max_end_here = 0
    for i in range(len(arr)):
        max_end_here = max_end_here + arr[i]
        if max_end_here < 0 :
            max_end_here = 0
        if max_so_far < max_end_here:
            max_so_far = max_end_here
    
    return max_so_far


