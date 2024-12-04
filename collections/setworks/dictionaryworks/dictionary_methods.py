
#dictionary_methods
#employee id,name,department,age,salary

employee={"id":234,"name":"rahul","department":"hr","age":32,"salary":34000}

#print(employee.get("salary"))

employee.pop("salary")

print(employee)


#keys///////////

for k in employee.keys():

    print(k)

#values//////////

for v in employee.values():

    print(v)

#print keys and values

for k,v in employee.items():

    print(k,v)    