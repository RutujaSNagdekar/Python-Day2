
from abc import ABC, abstractmethod

class Customer:
    def __init__(self, custld, custName):
        self.custld =custld
        self.custName=custName

    def display_details(self, custid ,custName):
        print( self.custld)
        print(self.custName)

    @abstractmethod
    def calculateAmount(self,interest, year):
        pass

class Regular_Customer(Customer):
    def __init__(self, custld, custName, Amount, custType):
        super().__init__(custld, custName)
        self.interest = None
        self.year = None
        self.Amount = Amount
        self.custType = custType

    def calculateAmount(self,interest, year):
        self.year = year
        self.interest = interest
        si = (self.Amount* self.year*self.interest)/100
        print("Customer ID:",self.custld)
        print("Customer Name:", self.custName)
        print("Customer Amount:", self.Amount)
        print("Customer Type:", self.custType)
        print("Interest for Regular Customer: ", si)



class Privilege_Customer(Customer):
    def __init__(self, custld, custName, Amount, custType):
        super().__init__(custld, custName)
        self.interest = None
        self.year = None
        self.Amount = Amount
        self.custType = custType

    def calculateAmount(self, interest, year):
        self.year = year
        self.interest = interest
        si = (self.Amount* self.year*self.interest)/100
        print("Customer ID:", self.custld)
        print("Customer Name:", self.custName)
        print("Customer Amount:", self.Amount)
        print("Customer Type:", self.custType)
        print("Interest for Privilege Customer: ", si-200)


print("For Regular User")
regular = Regular_Customer(1,"Rutuja",10000, "CDAC")
regular.calculateAmount(20,3)
print()
print("For Privilege User")
privilege = Privilege_Customer(1,"Rutuja",10000, "CDAC")
privilege.calculateAmount(20,3)




