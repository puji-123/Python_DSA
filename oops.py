#encapsulation
"""class A:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
a=A("puji",21,"male")
print(a1.name)
class A:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender
    def display(self):
        print(self.__name)
        print(self.__age)
        print(self.__gender)
    def setage(self,age):
        self.__age= age
    def getage(self):
        print(self.__age)
        
a=A("puji",21,"female")
a.display()
a.setage(33)
a.getage()
a.display()
from abc import ABC abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcal(self):
        pass
class SavingAccount(BankAccount):
    def interestcal(self):
        return self.__balance*0.05
#POLYMOPHISM
class Animal:
    def sound(self):
        print("animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class cat(Animal):
    def sound(self):
        print("meow")
a=cat()
a.sound()"""
  



