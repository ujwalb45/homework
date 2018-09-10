def arm(n):
	sum = 0
	temp = n
	while temp > 0:
	   digit = temp % 10
	   sum += digit ** 3
	   temp //= 10
	if n == sum:
	   print(n,"is an Armstrong number")
	else:
	   print(n,"is not an Armstrong number")

def main():
	n=input("Enter the number to check whether it is amstrong : ")
	arm(n)

if __name__=='__main__':
	main()



