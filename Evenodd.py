#even odd check using function
def chk_odd_even():
	num=int(input("Enter Number : "))
	if num%2==0:
		print("{} is Even".format(num))
	else:
		print("{} is odd".format(num))


run=int(input("How many time you want to Run this program : "))
i=0
while i<run:
	chk_odd_even()
	i +=1
