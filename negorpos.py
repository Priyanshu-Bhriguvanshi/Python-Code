#check number is positive or negative
def chk_pos_neg():
    num = int(input("Enter Number : "))
    if(num>0):
    	print("{} is positive ".format(num))
    elif(num<0):
        print("{} is negative ".format(num)) 
    else:
        print("Number is equal to zero")
        
run=int(input("How many time you Run this program : "))
i=0
while i<run:
	chk_pos_neg()
	i +=1        

