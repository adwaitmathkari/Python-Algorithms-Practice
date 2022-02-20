def f(n):
    i=len(str(n))
    for ch in str(n):
        i-=1
        if int(ch)%2!=0:
            maxOddIndex=i
            break
