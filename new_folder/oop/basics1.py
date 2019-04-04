class Trainee:
    def __init__(self, name, emp_id, age):
        self.__name = name
        self.__emp_id = emp_id
        self.age = age

    def get_name(self):
        return self.__name


    def get_emp_id(self):
        return self.__emp_id


#     def get_age(self):
#         return self.__age


    def set_name(self, value):
        self.__name = value


    def set_emp_id(self, value):
        self.__emp_id = value


#     def set_age(self, value):
#         self.__age = value


    def del_name(self):
        del self.__name


    def del_emp_id(self):
        del self.__emp_id


#     def del_age(self):
#         del self.__age

    name = property(get_name, set_name, del_name, "name's docstring")
    emp_id = property(get_emp_id, set_emp_id, del_emp_id, "emp_id's docstring")
#     age = property(get_age, set_age, del_age, "age's docstring")


rahul = Trainee("rahul", 1030600, 23)
rahul.age=90
rahul.__emp_id = 1030300

print(rahul.age)
print("get empId",rahul.get_emp_id())
print("rahul.__emp_id",rahul.__emp_id)
rahul._Trainee__emp_id=1010101
print("get empId",rahul.get_emp_id())
print(rahul.get_name())  

print(dir(rahul))  

"""thus the self.__emp_id attributes that was defined was simply stored as _Trainee__emp_id
   """  
print("dict: ", rahul.__dict__)
print("doc", rahul.__doc__)


rahul2 = Trainee("rahul2", 1030601, 25)

print(None+"hello world")
