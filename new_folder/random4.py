def change_list(num_list, nl2, nl3):
    num_list.append(20)
    num_list.append(30)
    nl2+=[20]
    nl3=nl3+[20]
    
def f1(a,b,*c):
    print("A IS ", a, "\nB IS ", b,  "\nC IS ", c)

# f1(1,2,3,4,5,6,7,8,9,123123)



var1=100
def f2():
    print(var1)
    var1=50
    print(var1)


print(var1)
f2()
print(var1)