#OOPR-Assgn-13
#Start writing your code here

class Classroom:
    classroom_list = []
    @staticmethod
    def search_classroom(class_room):
        for i in Classroom.classroom_list:
            if class_room.lower() == i.lower():
                return "Found"
        return -1
        