from re import fullmatch

passport_number=input("enter passport number")

pattern="[A-Z][1-9][0-9][0-9]{4}[1-9]"

matcher=fullmatch(pattern,passport_number)

if matcher==None:

    print("invalid")

else:

    print("valid")    





#The first character should be an uppercase alphabet.
#The next two characters should be a number, but the first character should be any number from 1-9 and the second character should be any number from 0-9.
#It should be zero or one white space character.
#The next four characters should be any number from 0-9.
#The last character should be any number from 1-9.