#Calculator Program
def cal():
    result=0
    num1=int(input("Enter First Number :  "))
    num2=int(input("Enter Second Number : "))
    op=input("Enter operator :: ")
    if op=="+":
        result=num1+num2
        print("Sum of {} and {} is : {}".format(num1,num2,result))
    elif op=="-":
        result=num1-num2
        print("Subtraction of {} and {} is : {}".format(num1,num2,result))
    elif op=="*":
        result=num1*num2
        print("Multiplication of {} and {} is : {}".format(num1,num2,result))
    elif op=="/":
        result=num1/num2
        print("Division of {} and {} is : {}".format(num1,num2,result))
    elif op=="%":
    	result=num1%num2
    	print("Mod of {} and {} is : {}".format(num1,num2,result))
    else:
        print("Invalid operator")

cal()
