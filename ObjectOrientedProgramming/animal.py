
class Animal:

    def __init__(self,name,species):
        
        self.name=name

        self.species=species

    def __str__(self):

        return self.name
    
class Lion(Animal):

    def __init__(self,name,species):

        super().__init__(name,species)

    def sound(self):

        print("roar is the sound of lion") 

lion_instance=Lion("lion","carnivous")

print(lion_instance)

lion_instance.sound()


class Cat(Animal):

    def __init__(self, name, species):

        super().__init__(name, species)

    def sound(self):

        print("meow is the  sound of cat") 

cat_instance=Cat("cat","carnivous")

print(cat_instance)

cat_instance.sound()