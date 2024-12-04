
f_read=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\words.txt","r")

f_palindrome=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\palindrome.txt","w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

       f_palindrome.write(word+"\n")

f_read.close()

f_palindrome.close()


    