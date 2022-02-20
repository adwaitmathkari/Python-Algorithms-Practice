#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_name(self):
        return self.__name


    def get_gender(self):
        return self.__gender


    def set_name(self, value):
        self.__name = value


    def set_gender(self, value):
        self.__gender = value


    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")      
            