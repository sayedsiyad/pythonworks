
f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)    