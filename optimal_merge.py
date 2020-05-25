'''
OPTIMAL MERGE PETTERN
PARADIGM - GREEDY
Date : 12-Feb-2020
Name - Harshit Singhal
'''


'''
	Another problem statement may be :
		Connect n rope with minimum cost where cost of connecting two rope is the sum of lwngth of rope
'''
def return_2_min(original_arr):
	arr = list(original_arr)
	min1 = min(arr)
	arr.remove(min1)
	min2 = min(arr)
	return min1,min2	
		
def cost_of_merging(size_of_lists):
	
	total_cost = 0
	while(len(size_of_lists) > 1):
		min1, min2 = return_2_min(size_of_lists)
		total_cost = total_cost + min1 + min2
		size_of_lists.remove(min1)
		size_of_lists.remove(min2)
		size_of_lists.append((min1+min2))
	print("MINIMUM COST OF MERGING OF GIVEN SEZE OF ARRAYS : {}".format(total_cost))


sizes = [20,30,10,5,30]
cost_of_merging(sizes)
	
	
	
	
	
