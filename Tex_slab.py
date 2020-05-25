

def find_tax(n):
	
	initial_money = n
	
	if(n > 1500000):
		tax = n * 0.3
		print(initial_money-tax)
		return
	

	n = n-250000
	tax = 0
	count = 1
	c = 2;
	
	while(n>0):
		if(n>250000):
			tax = tax + 250000*(0.05*count)
			count += 1
		else:
			tax = tax + n * (0.05*count)
			count = count + 1
		n = n - 250000
	print(tax)
	
find_tax(1500000)
