y=input('do you want to square a number? (y or n)  ')
while y=="y":
    ans=0
    x=int(input('enter the no you want to square  '))
    itr=x
    while itr>0:
        ans=ans+x
        itr-=1
    print('the square is  '+ str(ans))
    y=input('Do you want to square again? (y or n) ')
print('Thank you')

