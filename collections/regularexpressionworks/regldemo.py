
from re import finditer

text="fatcatrunsveryfasttocaththerat"

matcher=finditer("at",text)

for obj in matcher:

    print(obj.start(),obj.group())