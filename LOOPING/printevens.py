start=int(input("enter start number"))

end=int(input("enter the end number"))

if  start<end:

    for num in range(start,end+1,1):

        print(num)

else:

    for num in range(start,end-1,-1):

     print(num)                
