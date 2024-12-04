

employee={"eid":103,"name":"rahul","salary":23000,"department":"IT","experience":7}

print(employee["salary"])

employee["contact"]=9874567890

print(employee)

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000


if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)    
