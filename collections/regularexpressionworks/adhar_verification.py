from re import fullmatch

adhar_number=input("enter adhar number")

pattern="[2-9][0-9]{3}[\s][0-9]{4}[\s][0-9]{4}"

matcher=fullmatch(pattern,adhar_number)

if matcher==None:

    print("invalid")

else:

    print("valid")    






#It should have 12 digits.
#It should not start with 0 and 1.
#It should not contain any alphabet and special characters.
#It should have white space after every 4 digits.