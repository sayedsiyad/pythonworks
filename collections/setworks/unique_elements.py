
#arr=[100,10,10,20,30,40,50,40]

#100,10,20,30,40,50

#st=set()

#for num in arr:

#    st.add(num)
    
#print(st)


st1={10,20,30,40,50}

st2={10,20,60,70,80}

#intersection_set=st1.intersection(st2)

#print(intersection_set)

union_set=st1.union(st2)

print(union_set)

difference_set=st1.difference(st2)

print(difference_set)

st1.remove(50)

print(st1)