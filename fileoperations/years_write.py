
f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\years.txt","w")

for year  in range(1800,2024):

    f.write(str(year)+"\n")

f.close()    