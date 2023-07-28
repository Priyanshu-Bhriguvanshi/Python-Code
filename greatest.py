#greatest number
def gret():
    num1=int(input("Enter First number :: "))
    num2=int(input("Enter second number :: "))
    if(num1<num2):
        print("{} is greater than {} ".format(num2, num1)) 
    else:
        print("{} is greater than {} ".format(num1, num2)) 

gret()
