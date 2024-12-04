class Person:
    
    name:str

    age:int


    def __init__(self,name,age):
        
        self.name=name

        self.age=age

    def display_person_info(self):

        print(self.name,self.age)    


class Employee:

    emp_id:int

    salary:int

    def __init__(self,emp_id,salary):

        self.emp_id=emp_id

        self.salary=salary

    def display_employee_info(self):

        print(self.emp_id,self.salary)

class Manager:

    department:str

    def __init__(self,name,age,emp_id,salary,department):

        Person.__init__(name,age)

        Employee.__init__(emp_id,salary)

        self.department=department

    def display_manager_info(self):

        self.display_person_info()

        self.display_employee_info()

        print(self.department)


manage_instance=Manager("hari",32,"e01",54000,"hr")

manage_instance.display_manager_info()





