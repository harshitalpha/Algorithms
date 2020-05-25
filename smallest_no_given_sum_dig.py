'''
SMALLEST NUMBER WITH GIVEN NUMBER OF DIGIT AND SUM OF DIGIT
PARADIGM - GREEDY
Date : 14-Feb-2020
Name - Harshit Singhal
'''

def find_number(s,d):

	'''
		We approch the problem by greedy method.
		eg : s = 20 , d = 3
			make an arr of size d = [0,0,0]
			sum = sum -1  now sum = 19
			iterate to the loop rerverse order
				if sum is grater or equal to 9
					arr[last] = 9
					sum = sum - 9
				else
					arr[current index] = sum
					sum = 0
			now we add one to arr start because we substract 1 from sum at begining at keep no. smallest
	'''
	
	print("SUM =    {}".format(s))
	print("DIGITS = {}".format(d))
	if(s == 0):
		if(d==1):
			print("ANSWER IS : 0")
			return
		else:
			print("NOT POSSIBLE")
			return
	
	if(s > d*9):
		print("NOT POSSIBLE")
		return
	
	digit = [0] * d
	
	s = s - 1
	
	
	for i in range(d-1,-1,-1):
		if(s >= 9):
			digit[i] = 9
			s -= 9
		else:
			digit[i] = s
			s = 0
			break
			
	digit[0] = digit[0] + 1
	
	
	print("ANSWER IS : ",end = "")
	for i in digit:
		print(i,end = "")
	


def main():

	print("\nTEST CASE 1")
	s = 20
	d = 3
	find_number(s,d)

	print("\n\nTEST CASE 2")
	s = 9
	d = 2
	find_number(s,d)


	print("\n\nTEST CASE 3")
	s = 25
	d = 3
	find_number(s,d)

	print("\n\nTEST CASE 4")
	s = 25
	d = 4
	find_number(s,d)

	print("\n\nTEST CASE 5")
	s = 25
	d = 5
	find_number(s,d)
	

if __name__ == "__main__":
	main()
		
		
