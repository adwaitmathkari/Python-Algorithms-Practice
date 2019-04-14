#OOPR-Assgn-10

class CallDetail:
    def __init__(self,phoneno, called_no, duration, call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration =duration
        self.__call_type = call_type
    
    def getcalledno(self):
        return self.__called_no
        
class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        al=[]
        for i in list_of_call_string:
            params = i.split(",")
            assert len(params)==4
            al.append(CallDetail(params[0], params[1], params[2], params[3]))
        
        self.list_of_call_objects = al
    
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330045003,6,ISD'

list_of_call_string=[call,call2,call3]
u1 = Util()
u1.parse_customer(list_of_call_string)
for i in u1.list_of_call_objects:
    print(i.getcalledno())
    
    
    
    
    
    
    
    
