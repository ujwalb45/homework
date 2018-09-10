def dbd(n):
	evensum=0
	oddsum=0
	k=0
	while(n!=0):
		k=n%10
		n=n/10
		if k%2==0:
			evensum=evensum+k
		else:
			oddsum=oddsum+k
	print("Diff bet evensum and oddsum is : ",evensum-oddsum)
def main():
	n=input("Enter the number : ")
	dbd(n)

if __name__=='__main__':
	main()
