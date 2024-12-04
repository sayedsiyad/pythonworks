
colors={"red","green","blue"}

colors.add("yellow")

print(colors)

st1={1,2,3}

st2={1,2,3,4,5}

print(st1.issubset(st2))

print(st2.issuperset(st1))

st1={1,2,3,10,20}

st2={1,2,3,4,5}

#10,20,4,5

symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)

#update/////

st1={1,2,3,10,20}

st2={1,2,3,4,5}

st1.update(st2)

print(st1)

text="this is a test to remove duplicate words this test is  simple"

#split text words 

words=text.split(" ")

print(set(words))