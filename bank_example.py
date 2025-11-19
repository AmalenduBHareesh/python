class Bank_V1():
    bank_name = 'sbi'
    bank_branch = 'kisikulan'
    bank_roi = 5
    def __init__(self, cn, ca, cb):
        self.cname = cn
        self.camount = ca
        self.cbalance = cb
    def customer_details(self):
        print(f'name of customer is {self.cname}')
        print(f'account of customer is {self.camount}')
        print(f'balance of custome is {self.cbalance}')
    @staticmethod
    def get_int_value():
        iv = int(input())
        return iv
    def withdraw(self):
        print('enter amount to withdraw')
        amount = self.get_int_value()
        if amount <= self.cbalance:
            self.cbalance -= amount
            print('withdrawal is successful')
        else:
            print('insufficient balance')
        print(f'balance is {self.cbalance}')
    @classmethod
    def bank_details(cls):
        print(f'name of the bank is {cls.bank_name}')
        print(f'branch of the bank is {cls.bank_branch}')
        print(f'roi of the bank is {cls.bank_roi}')
    @classmethod
    def modify_soi(cls):
        print('enter new roi')
        nsoi = cls.get_int_value()
        cls.bank_soi = nsoi
        print('roi is changed')
class Bank_V2(Bank_V1):
    def deposite(self):
        print ('Enter the amount to deposite')
        amount=self.get_int_value()
        self.cbalance+=amount
        print('deposite is successfull')  
        # print(self.cbalance) 



customer1 = Bank_V1('Ammu', 12345, 5000)
# customer1.customer_details()
# customer1.withdraw()
customer2 = Bank_V2('Ammu', 12345, 5000)
# customer2.withdraw()  
customer2.deposite()  

