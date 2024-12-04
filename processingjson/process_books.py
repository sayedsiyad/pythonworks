
from json  import  load

f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\books.json")

data=load(f)

all_titles=[book.get("title")for  book in data]

page_filter=[book.get("title")for book in data if book.get("pages")<250]

all_genres=[book.get("genre")for book in data]

genre_count={genre:all_genres.count(genre)for genre in all_genres}

#print(set(all_genres))
#print(all_genres)

#cosly book

costly_book=max(data,key=lambda d:d.get("price"))

#print(costly_book)

#author with more than one book

all_authors=[book.get("author")for book in data]

#print(all_authors)

author_count={auth:all_authors.count(auth)for auth in all_authors}

print([k for k,v in author_count.items() if v>1])



