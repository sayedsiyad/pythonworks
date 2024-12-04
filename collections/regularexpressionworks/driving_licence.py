from re import fullmatch

driving_licence=input("enter driving licence")

pattern="(KL)[-][0-9]{13}"

matcher=fullmatch(pattern,driving_licence)

if matcher==None:

    print("invalid")

else:   

    print("valid")








#The first two characters should be upper-case alphabets that represent the state code.
#The next two characters should be digits that represent the RTO code.
#The next four characters should be digits that represent the license issued in a year.
#The next seven characters should be any digits from 0-9.