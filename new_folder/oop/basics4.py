


class Animal:
    def __init__(self, eyes):
        self.__eyes = eyes
        self.__life = True

    def get_eyes(self):
        print("animal method called")
        return self.__eyes


    def __get_life(self):
        return self.__life
    def get_life(self):
        return self.__get_life()
    
   
class Mammal:
    def __init__(self):
        self.evolution_level = "HIGH"
        self.biggest_mammal = "Whale"
        
    def get_eyes(self):
        print("mammals have 2 eyes")
        return 2
 
class Rabbit(Animal, Mammal):
    def __init__(self):
        Animal.__init__(self,2)
        Mammal.__init__(self)
        self.legs = 4
        
    def get_eyes(self):
        print("rabbit method calllled")
        Mammal.get_eyes(self)
        return super().get_eyes()
        
# print(dir(Rabbit))    
print(Rabbit().get_eyes())
# print(Rabbit().biggest_mammal)
    










# #Object creation
# class Customer:
#     def __init__(self, name,cust_type,bill):
#         self.name = name
#         self.bill = bill
#         self.cust_type=cust_type
# 
#     def calulate_bill(self):
#         tax1=Tax(self.cust_type)
#         final_bill=self.bill*tax1.tax_details(self.cust_type)
#         return final_bill
# 
# class Tax:
#     def __init__(self,cust_type):
#         self.cust_type=cust_type
# 
#     def tax_details(self,cust_type):
#         if(cust_type=="Student"):
#             return 5
#         else:
#             return 10
# 
# 
# cust1=Customer("Maddy","Student",100)
# print(cust1.calulate_bill())




# class Customer:
#     def __init__(self, name, age, phone_no, address):
#         self.name = name
#         self.age = age
#         self.phone_no = phone_no
#         self.address = address
# 
#     def view_details(self):
#         print (self.name, self.age, self.phone_no)
#         for i in range(2):
#             print (self.address.getdetails()[i], end=" ")
# 
# class Address:
#     def __init__(self, door_no, street, pincode):
#         self.__door_no = door_no
#         self.__street = street
#         self.__pincode = pincode
#     def getdetails(self):
#         return (self.__door_no,self.__street, self.__pincode)
#     def update_address(self):
#         pass
# 
# add1=Address(123, "5th Lane", 56001)
# cus1=Customer("Jack", 24, 1234, add1)
# 
# cus1.view_details()
