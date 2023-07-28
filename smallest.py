#smallest number
def small():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter Second Number : "))
    if num1<num2:
    	print("{} smallest than {} ".format(num1,num2))
    elif num1>num2:
    	print("{} smallest than {} ".format(num2,num1))
    else:
        print("Both number are equal")
        
small()
