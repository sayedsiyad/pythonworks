#factorial

def factorial(num):

    fact=1

    for i in range(1,num+1):

        fact=fact*i

        return fact
    
    result=factorial(3)

    print(result)


#create a function num_chk return odd if number is odd else return even

def num_chk(number):

    return "even" if number%2==0 else "odd"

print(num_chk(10))

#q2) create a function max_two with two parameter num1,num2 return largest number


def max_two(num1,num2):

    return num1 if num1>num2 else num2

print(max_two(100,200))

"""create a function multiplication_table(number,n)
print multiplication table of number till n"""

#multiplication_table(3,50)

def multiplication_table(number,n):

    for i in range(1,n+1):

      print(f"{i} * {number} = {i*number}")

multiplication_table(3,100)     

#create a function exponent with two parameter num1,n

def expo(number,n=2):

    return number**n

print(expo(6))

#create a function random_numbers(start,end,step)

#print numbers from start to end
#random_numbers(1,7,2) #1,3,5

def random_numbers(start,end,step=1):

    while