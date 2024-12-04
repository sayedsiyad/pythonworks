
from re import findall

f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\regex_fileworks\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"     

dates=findall(pattern,content)

for d in dates:

    print(d)