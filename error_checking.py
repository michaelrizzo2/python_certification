def sum(number1,number2):
    if type(number1)!=int:
        number1=int(input("Please enter a number"))
        sum(number1,number2)
    elif type(number2)!=int:
        print("number is not there")
    else: 
        print(number1+number2)
number1=input("Please enter a number\n")
#use try and exept when the situation is out of your control.
sum(number1,12)
#The rest of section 6 is useless because the needed files are no there.