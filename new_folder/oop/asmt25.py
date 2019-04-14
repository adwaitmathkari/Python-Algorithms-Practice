#OOPR-Assgn-25
#Start writing your code here


class FruitInfo:
    __fruit_name_list=["Apple","Guava", 
                       "Orange","Grape","Sweet Lime"]
    __fruit_price_list = [200 ,80,70 ,110 ,60]
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
    @staticmethod
    def get_fruit_price(fruit_name):
        for i in range(len(FruitInfo.__fruit_name_list)):
            if FruitInfo.__fruit_name_list[i]==fruit_name:
                return FruitInfo.__fruit_price_list[i]            
        return -1


class Purchase:
    __counter = 101
    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def get_purchase_id(self):
        return self.__purchase_id


    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity

         
    def calculate_price(self):
        price=FruitInfo.get_fruit_price(self.__fruit_name)
        if price ==-1:
            return -1
        else:
            total_price = price*self.__quantity
            maximum=True
            minimum=True
            for i in FruitInfo.get_fruit_price_list():
                if price<i:
                    maximum=False
                elif price>i:
                    minimum=False
            if maximum and self.__quantity>1:
                total_price *=.98
            elif minimum and self.__quantity>=5:
                total_price *=.95
            if self.__customer.get_cust_type()=="wholesale":
                total_price*=.9
            self.__purchase_id="P"+str(Purchase.__counter)
            Purchase.__counter+=1
            return total_price
    


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name


    def get_cust_type(self):
        return self.__cust_type       
            
            
c1 = Customer("John", "wholesale")
p1 = Purchase(c1, "Apple", 100)  
print(p1.calculate_price())
        
        
   