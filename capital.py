#capital letter and smallest letter
def chk_cap():
    capital=0
    lower=0
    str=input("Enter any string : ")
    for i in str:
        if ord(i)>=65 and ord(i)<=90:
            capital +=1
        elif ord(i)>=97 and ord(i)<=122:
            lower +=1
        else:
            pass
    print(" total capital letter in {} is {} ".format(str, capital))
    print(" total small letter in {} is {} ".format(str, lower))
            
chk_cap()
