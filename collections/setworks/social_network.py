
users=["rahul","rohit","kohli","rishabh","sanju","pandya","siraj"]

rahul_followers=["rahul","rohit","kohli","rishabh"]

sanju_followers=["sanju","rohit","kohli"]

#mutual_friends

rahul_follow_suggestion=set(users).difference(set(rahul_followers))

mutual=set(rahul_followers).intersection(set(sanju_followers))

print(mutual)


