
num1=int(input("enter number1:"))

num2=int(input("enter number2:"))

gcd=1

min_num=min(num1,num2)

for i in range(1,min_num+1):

    if num1%i==0 and num2%i==0:
    

     gcd=1

print(gcd)

