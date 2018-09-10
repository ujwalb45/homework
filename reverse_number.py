def rev(a):
	rev=0
	while a!=0:
		rem=a%10
		a=a/10
		rev=(rev*10)+rem
	print("The reverse number is : ",rev)	

def main():
	n=input("Enter the number to reverse it")
	rev(n)

if __name__=='__main__':
	main()
