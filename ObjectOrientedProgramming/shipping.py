
class shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping:

    def calculate_shipping_cost(self,weight):

        print(weight*20)

class StanderdShipping:

    def calculate_shipping_cost(self,weight):

        print(weight*10)

express_instance=ExpressShipping()

express_instance.calculate_shipping_cost(10)

standerd_instance=StanderdShipping()

standerd_instance.calculate_shipping_cost(10)