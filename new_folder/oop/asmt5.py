#OOPR-Assgn-5
#Start writing your code here


class Vehicle():
    
    id = 1000000
    @staticmethod
    def generateid():
        retid = bin(Vehicle.id)
        Vehicle.id+=1
        return retid
    
    def __init__(self, cost, type):
        self.__cost=cost
        self.__premium_amt = None
        self.__id = Vehicle.generateid()
        if(type =="Two Wheeler" or type=="Four Wheeler"):
            self.__type = type
        else:
            raise ValueError("the type of the vehicle must be Two Wheeler or Four Wheeler")

    def get_cost(self):
        return self.__cost


    def get_premium_amt(self):
        return self.__premium_amt


    def get_type(self):
        return self.__type


    def set_cost(self, value):
        self.__cost = value


    def set_premium_amt(self, value):
        self.__premium_amt = value


    def set_type(self, value):
        self.__type = value

    def calculate_premium(self):
        if self.__type=="Two Wheeler":
            pr = 0.02
            print(pr,self.__type)
        else:
            pr = 0.06
            print(pr,self.__type)
            
        self.set_premium_amt( pr*self.__cost)
    

    def display_vehicle_details(self):
        print("Vehicle with id", self.__id, "of type", self.__type, "costing", self.__cost, "has a premium amt of", self.__premium_amt)
        

v1 = Vehicle(84000, "Two Wheeler")
v2 = Vehicle(700000, "Four Wheeler")

v1.calculate_premium()
v2.calculate_premium()
print(v1.get_premium_amt())
print(v2.get_premium_amt())
print(v1._Vehicle__id)
print(v2._Vehicle__id)
