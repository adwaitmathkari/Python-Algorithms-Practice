#OOPR-Assgn-15
#Start writing your code here

class Parrot:
    __counter=0
    def __init__(self, name, color):
        Parrot.__counter+=1
        self.__name=name
        self.__color = color
        self.__unique_number = Parrot.__counter

    def set_unique_number(self, value):
        self.__unique_number = value


    def get_name(self):
        return self.__name


    def get_color(self):
        return self.__color


    def get_unique_number(self):
        return self.__unique_number


    def set_name(self, value):
        self.__name = value


    def set_color(self, value):
        self.__color = value


p1 = Parrot("j", "blue")
p2 = Parrot("po", "red")
print(p1.get_unique_number())
