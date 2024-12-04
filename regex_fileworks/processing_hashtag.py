from re import  finditer

f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\regex_fileworks\\hashtag.txt")

for line in f:

    hashtag=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,hashtag)

    for obj in matcher:

       print(obj.group())


