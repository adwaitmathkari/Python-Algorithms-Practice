#OOPR-Exer-13
#Start writing your code here

from abc import abstractmethod

class DirectToHomeService:
    __counter=101
    def __init__(self, consumer_name):
        self.consumer_number= DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        self.__consumer_name = consumer_name
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

    def get_consumer_number(self):
        return self.__consumer_number


    def get_consumer_name(self):
        return self.__consumer_name


class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if self.__base_pack_name not in ["Silver", "Gold", "Platinum"]:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")
            
    
    @abstractmethod
    def calculate_monthly_rent(self):
        if self.validate_base_pack_name() and self.__subscription_period()>=1 and self.__subscription_period()<=24:
            monthly_rent = {"Silver":350.00, "Gold":440.00, "Platinum": 560.00}[self.__base_pack_name]
            discount=0
            if self.get_subscription_period()>12:
                discount = monthly_rent
            final_monthly_rent = ((monthly_rent * self.__subscription_periodperiod)-discount)/self.__subscription_period
            return final_monthly_rent
        else:
            return -1
