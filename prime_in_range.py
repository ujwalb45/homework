def prime_range(a,b):
	print("The prime numbers in given range are as follows : ")
	for x in range(a,b+1):
		if x>1:
			for y in range(2,x):
				if (x%y)==0:
					break
			else:
				print(x)
def main():
	lb=input("Enter the lower bound")
	ub=input("Enter the upper bound")
	prime_range(lb,ub)	

if __name__=='__main__':
	main()

