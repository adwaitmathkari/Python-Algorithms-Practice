def f1():
    for i in 1,2,3,4,5,6:
        print(i)
        if (i==3):
            break
        print(i)
    print("outside loop")
def f2():
    for i in 1,2,3,4,5,6:
        print(i)
        if (i==3):
            continue
        print(i)
    print("outside loop")

def f3():
    for i in 1,2,3,4:
        for j in "a","b", "c":
            print(i)
            if(i==3):
                continue
            print(j)


f2()
