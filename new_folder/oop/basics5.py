from abc import ABCMeta, abstractmethod

class Customer(metaclass=ABCMeta):
    def __init__(self, name, list_of_games):
        self.__name = name
        self.__list_of_games = list_of_games
        self.__ticket = None
        self.__points_earned = None
        self.__food_coupon = None
    
    @abstractmethod
    def m1(self):
        print("abstract method 1")


class RetailCustomer(Customer):
    def m1(self):
        super().m1()

rc1=RetailCustomer("jonya", ["football", "fencing"])
# rc1.m1()

a=Exception()
print(dir(a))
print(a.args, a.with_traceback("something over here"))
raise a


class Parent(metaclass=ABCMeta):
    def __init__(self):
        print(100)

    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(10)
    def show(self):
        print(" _/\_")

obj=Child()
obj.show()





# 
# class nEx(Exception):
#     pass
# 
# n1=nEx("message here will go to the freakin' exception")
# 
# try:
#     raise n1
# except nEx as e:
#     print(e)
