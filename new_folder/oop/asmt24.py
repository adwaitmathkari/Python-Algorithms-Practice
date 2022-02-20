#OOPR-Assgn-24
#Start writing your code here

class Apparel:
    counter=100
    def __init__(self, price, item_type):
        Apparel.counter+=1
        self.__price = price
        self.__item_type = item_type
        self.__item_id = item_type[0].upper() + str(Apparel.counter)

    def get_item_type(self):
        return self.__item_type


    def get_item_id(self):
        return self.__item_id


    def get_price(self):
        return self.__price


    def set_price(self, price):
        self.__price = price

        
    def calculate_price(self):
        self.__price = 1.05*self.__price
        
    
    
class Cotton(Apparel):
    def __init__(self, price ,discount):
        super().__init__(price, "Cotton")
        self.__discount = discount

    def get_discount(self):
        return self.__discount

    
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price = price*(100-self.__discount)/100*1.05
        self.set_price(price)
    

class Silk(Apparel):
    def __init__(self, price ):
        super().__init__(price, "Silk")
        self.__points = None
        
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        self.__points = 10 if price>10000 else 3
        self.set_price(price*1.1)

    def get_points(self):
        return self.__points 

    


c1 = Cotton(2000, 10)
s1 = Silk(15000)
c2=Cotton(5000, 5)
s2=Silk(8000)

s1.calculate_price()
print(s1.get_price(), " price<<silk>> points", s1.get_points())
c1.calculate_price()
print(c1.get_price())
    
print("----------")
s2.calculate_price()
print(s2.get_price(), " price<<silk>> points", s2.get_points())
c2.calculate_price()
print(c2.get_price())
    
    