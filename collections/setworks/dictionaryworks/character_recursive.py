
text="ABAABBC"

words=text.split(" ")

def get_count(char):

    return text.count(char)

most_freequent_character=max(text,key=get_count)

print(most_freequent_character)


least_recursive_character=min(text,key=get_count)

print(least_recursive_character)







