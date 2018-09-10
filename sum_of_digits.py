def dbd(n):
	sum=0
	while(n!=0):
		sum=sum+(n%10)
		n=int(n/10)
	print("Sum of the digits is : ",sum)
def main():
	n=input("Enter the number : ")
	dbd(n)

if __name__=='__main__':
	main()
