from abc import ABC,abstractmethod 

class bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):

        pass

class Hunter(bike):

    def start(self):
        print("Hunter  start  method")

    def accelerate(self):
        print("Hunter accelerate method")

    def stop(self):
        print("Hunter stop")        


hunter_instance=Hunter()

hunter_instance.start()