
text="ABABBCCDDE"

#character_freequency(A:2,B:3,,,)

character_freequency={ch:text.count(ch)for ch in text}

print(character_freequency)

#non recursive elements

for k,v in character_freequency.items():

    if v==1:

      print(k)