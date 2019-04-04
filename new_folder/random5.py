

def g1():
    var1=100
    def f2():
        global var1
        print(var1)
        var1=50
        print(var1)
    # 
    # print("out 1",var1)
    # f2()
    # print("out 2", var1)    
    for i in range(10):
        pass
    print(i)


#PF-Exer-30

def find_average(mark_list):
    total=0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list1[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except NameError as e:
        print(e)    

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))



