
#lambda function for adding 2 numbers

add=lambda n1,n2:n1+n2

print(add(10,20))

#lambda function for subtracting 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(20,10))

#lambda function for finding cube of a number

cube=lambda n:n**3

print(cube(4))

#lambda function for finding square of a number

square=lambda n:n**2

print(square(4))

#max two////



max_two=lambda str1,str2:str1 if len(str1) > len(str2) else str2

print(max_two("hai","morning"))

#min two////




min_two=lambda str1,str2:str1 if len(str1) <len(str2) else str2

print(min_two("morning","hai"))

#smart sub//




smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100))


#get length///////



words=["hello","hai","morning","test","apple"]

def get_length(word):

    return len(word)

get_length=lambda word:len(word)

print(max(words,key=get_length))