#PF-Tryout
#Start writing your code here
def displayGrade(marks):
    marks=int(marks)
    if(marks<0 or marks >100):
        grade="Z"
    elif(marks<65):
        grade="D"
    elif(marks<73):
        grade = "C"
    elif(marks<80):
        grade="B"
    else:
        grade = "A"
    return grade

for i in range(10,-2,-1):
    print(i)
    