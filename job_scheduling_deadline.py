'''
JOB SCHEDULING WITH DEADLINE
PARADIGM - GREEDY
Date : 12-Feb-2020
Name - Harshit Singhal
'''

def assign_jobs(profit, deadline):

	'''
		The idea to implement is that take two list of profit and deadline
		we make list of index = [0,1,2,...]
		then we will sort index list according to profit matrix
		eg : 
			index = [0,1,2,3]
			ratio = [4,6,1,3]
			after sorting 
			index = [1,0,3,2]
			6 is largest and index corrosponding to 6 place first 
		
		
		
	'''

	index = list(range(len(deadline)))
	
	max_dead = max(deadline)
	
	job_sequence = [None] * max_dead
	
	index.sort(key = lambda i:profit[i], reverse = True)
	
	print("profit : {}".format(profit))
	
	print("deadline : {}".format(deadline))
	
	for i in index:
		d = deadline[i]
		for j in range(d-1, -1,-1):
			if(job_sequence[j] is None):
				job_sequence[j] = i
				break;
	max_profit = 0
	for i in job_sequence:
		max_profit = max_profit + profit[i]

	print("JOB ARE TO BE DONE IN THE ORDER AS FOLLOWS \n{}".format(job_sequence))
	print("FOR MAXIMUM PROFIT OF {}".format(max_profit))


profit = [20,15,10,5,1]

deadline = [2,2,1,3,3]

assign_jobs(profit, deadline)
