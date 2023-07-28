#vowel check
def vowel():
    vowel_count=0
    str=input("Enter any string : ")
    lostr=str.lower()
    for i in lostr:
        if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            vowel_count +=1
        else:
            pass
    print('Total vowel in "{}" is {}'.format(str,vowel_count))

vowel()
