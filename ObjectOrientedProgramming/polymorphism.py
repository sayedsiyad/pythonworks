
#method3 over_loading(same method name and  different number of parameters)

class operations:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)   


obj=operations()

obj.add(10,20,30)