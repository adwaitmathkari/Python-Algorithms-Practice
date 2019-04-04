#OOPR-Assgn-17
#Start writing your code here

class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address
    
    def validate_customer_id(self):
        return self.__customer_id<=199999 and self.__customer_id>=100000
 
    
    def get_customer_id(self):
        return self.__customer_id


    def get_customer_name(self):
        return self.__customer_name


    def get_address(self):
        return self.__address


class Freight:
    counter = 198
    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__recipient_customer = recipient_customer 
        self.__from_customer = from_customer 
        self.__weight = weight 
        self.__distance = distance
        self.__freight_id = None
        self.__freight_charge = None

    def get_recipient_customer(self):
        return self.__recipient_customer


    def get_from_customer(self):
        return self.__from_customer


    def get_weight(self):
        return self.__weight


    def get_distance(self):
        return self.__distance


    def get_freight_id(self):
        return self.__freight_id

    
    def validate_weight(self):
        return self.__weight%5==0
    
    def validate_distance(self):
        return self.__distance<=5000 and self.__distance>=500
        
    def forward_cargo(self):
        if (self.__recipient_customer.validate_customer_id() and 
            self.__from_customer.validate_customer_id() and 
            self.validate_distance() and self.validate_weight()):
            Freight.counter+=2
            self.__freight_id = Freight.counter
            freight_charge = 150*self.__weight + 60*self.__distance
            self.__freight_charge = freight_charge
        else:
            self.__freight_charge = 0
    
    def get_freight_charge(self):
        return self.__freight_charge
    


c1  = Customer(100000,"j", "kothrud")
c2= Customer(120000,"p", "kothrud")

f=Freight(c1,c2, 100, 2000)
f.forward_cargo()
print(f.get_freight_id())
f.forward_cargo()
print(f.get_freight_id())


        
        
        
        
        
        
        