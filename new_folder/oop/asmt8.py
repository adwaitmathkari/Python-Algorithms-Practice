#OOPR-Assgn-9
#OOPR-Assgn-8
#Start writing your code here

"""
Attributes
    (private)    
    student_id
    marks
    age

Methods
(public)   
     __init__()    Create and initialize all instance variables to None
    validate_marks()    If data is valid, return true. Else, return false
    validate_age()
    check_qualification()    
        Validate marks and age.
        If valid, check if marks is 65 or more.
        If so return true
        Else return false
        Else return false
    setter methods    Include setter methods for all instance variables to set its values
    getter methods    Include getter methods for all instance variables to get its values

"""


class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id=None
        self.__fees = None

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def validate_marks(self):
        return self.__marks>=0 and self.__marks<=100
    
    def validate_age(self):
        return self.__age>20
    
    def check_qualification(self):
        if (self.validate_age() and self.validate_marks()):
            return self.__marks>=65
        else:
            return False
    def choose_course(self, course_id):
        if course_id in [1001, 1002]:
            self.set_course_id(course_id)
            if self.__marks>85:
                self.set_fees(self.__fees*25/100)
            return True
        else:
            return False

    def get_course_id(self):
        return self.__course_id


    def get_fees(self):
        return self.__fees


    def set_course_id(self, course_id):
        self.__course_id = course_id


    def set_fees(self, fees):
        self.__fees = fees


#Implement Student class here
maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")



