class Bankaccount:


    def __init__(self,customer_name,mpin,account_type,balance):

        self.customer_name=customer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance

    def get_balance(self):

        print(self.__balance)

    def __str__(self):

        return self.customer_name

bank_account_instance=Bankaccount("hari",2345,"savings",45000)

bank_account_instance.get_balance()

