def fib(n):
	p=0
	q=1
	s=p+q
	print p
	print q
	print s
	sum=0
	while(sum<n-1):
		sum=s+q
		q=s
		s=sum
		print sum


def main():
	n=input("Enter the limit of the fibonacci series")
	fib(n)

if __name__=='__main__':
	main()
