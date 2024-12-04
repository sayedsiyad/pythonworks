class  Grandparent:

    def  m(self):

        print("Grandparent  class  m1 method")

class Parent():

    def m(self):

        print("parent class m2 method") 

#Error name ambiguity error[java]=>interface


class child(Grandparent,Parent):

    def m3(self):

        print("child class  m3 method") 

child_instance=child()

child_instance.m3()

child_instance.m()
