
text="this is a simple programming question to find word with maximum number of characters"

#step 1 split the words

words=text.split(" ")

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(max(words,key=get_length))

print(srt_words)









