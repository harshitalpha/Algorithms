'''
KNAPSACK PROBLEM
PARADIGM - GREEDY
Date : 12-Feb-2020
Name - Harshit Singhal
'''

def knapsack(profit, weights, max_weight):

	'''
		The idea to implement is that take two list of profit and weights
		we make list of index = [0,1,2,...]
		then we calculate the profit and weight ratio and store in list named ratio 
		then we will sort index list according to ratio matrix
		eg : 
			index = [0,1,2,3]
			ratio = [4,6,1,3]
			after sorting 
			index = [1,0,3,2]
			6 is largest and index corrosponding to 6 place first 
		
		for this we use following comand 
			index.sort(key = lambda i:ratio[i], reverse = True)
		
		we will use 'zip' some place in code 
		use of zip is that in iterable and return iterator
			>>> numbers = [1, 2, 3]
			>>> letters = ['a', 'b', 'c']
			>>> zipped = zip(numbers, letters)
			>>> zipped  # Holds an iterator object
			<zip object at 0x7fa4831153c8>
			>>> type(zipped)
			<class 'zip'>
			>>> list(zipped)
			[(1, 'a'), (2, 'b'), (3, 'c')]
		
		then we follow the regular approch of solving greedy problem
			
	'''

	print("WEIGHTS GIVEN =                   {}".format(weights))
	print("PROFIT  GIVEN =                   {}".format(profit))
	print("MAX WEIGHT CAN CARRY =            {}".format(max_weight))
	
	index = list(range(len(weights)))
	
	ratio = [v/w for v,w in zip(profit, weights)]
	
	index.sort(key = lambda i:ratio[i], reverse = True)
	
	ans_weights = [0] * len(weights)
	
	for i in index:
		if(weights[i] <= max_weight):
			ans_weights[i] = 1
			max_weight  = max_weight - weights[i]
		else:
			ans_weights[i] = float(float(max_weight) / float(weights[i]))
			break
	
	# Total Profit 
	final_profit = 0
	for i in range(len(weights)):
		final_profit = final_profit + (ans_weights[i] * profit[i])
	
	print("WEIGHT OF EACH OBJECT CAN CARRY = {}".format(ans_weights))
	print("FINAL PROFIT =                    {}".format(final_profit))	 


profit = [10,5,15,7,6,18,3]
weights = [2,3,5,7,1,4,1]
 
knapsack(profit,weights,15)
		
