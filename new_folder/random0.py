def tryit1():
    name=input("Enter your name")
    print("Hi your name is ",name)


def tryit2():
    for i in range(1,10000000):
        x=i*2.0
    print("Done")
    
# tryit2()
# tryit1()


#PF-Tryout

def func1():
    result_sum=0
    #Write the code to find the sum of numbers from 1 to 10000000
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    #Write the code to accept 5 numbers from user and find its sum
    print("Sum from func2:",result_sum)

#Modify the code given below to execute func1() and func2() in two separate threads
func1()
func2()

print("--------------------------")

print((1,-1)==(1,-1))