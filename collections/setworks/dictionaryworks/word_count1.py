
words=["hello","hai","hello","this","is","this","is","hello"]

word_freequency={w:words.count(w) for w in words}

print(word_freequency)

recursive_words=[k for k,v in word_freequency.items() if v>1]

print(recursive_words)

#most_recursive