number=int(input("enter the number"))

total=0

while(number!=0):

    digit=number%10

    digit_square=digit**2

    total=total+digit_square

    number=number//10

print(total)    



