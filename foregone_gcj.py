
t=int(input())

for i in range(t):
    s=input()
    a=''
    b=''
    
    for i in s:
        if i=='4':
            a+='3'
            b+='1'
        else:
            a+=i
            b+='0'
    a=int(a)
    b=int(b)
    print("Case #"+str(t)+ ": "+str(a)+ " "+ str(b))