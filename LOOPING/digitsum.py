number=int(input("enter the  number"))#234

total=0

while(number!=0):  #234!=0

    digit=number %10  #234%10=4

    total=total+digit  #0+4=4

    number=number//10  #234//10=23

print(total)    

