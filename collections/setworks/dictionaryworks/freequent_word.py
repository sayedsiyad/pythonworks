
text="this is a simple programming question to find word with maximum number of characters"

words=text.split(" ")

def get_count(w):

    return words.count(w)

freequent_word=max(words,key=get_count)

print({freequent_word:words.count(freequent_word)})