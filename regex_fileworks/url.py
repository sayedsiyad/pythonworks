from re import findall

f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\regex_fileworks\\url.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)





    
