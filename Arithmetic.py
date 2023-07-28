#Add Function
def sum():
    print("-----Sum Function Call -----")
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))
    total=num1+num2
    print("Sum of {} and {} is : {}".format(num1,num2,total))

#subtract function
def minus():
    print()
    print("-----Subtract Function Call-----")
    num1=int(input("Enter First Number :"))
    num2=int(input("Enter Second Number :"))
    total=num1-num2
    print("Subtraction of {} and {} is : {}".format(num1,num2,total))
    
#Multiplication Function
def mul():
    print()
    print("-----Multiplication Function Call-----")
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))
    total=num1*num2
    print("Multiplication of {} and {} is : {}".format(num1,num2,total))

#Division function
def div():
    print()
    print("-----Division Function Call-----")
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))
    total=round(num1/num2,2)
    print("Division of {} by {} is : {}".format(num1,num2,total))

#modles Function
def mod():
    print()
    print("-----Mod Function Call-----")
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))
    total=round(num1%num2,2)
    print("Mod : {}".format(total))

    

sum()
minus()
mul()
div()
mod()

