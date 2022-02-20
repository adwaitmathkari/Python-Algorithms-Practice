s='bobobfbobsbobnbob yu ()fubob'
count=0
n=0
k=len(s)
while n<k-1:
    if s[n]=='b' and s[n+1]=='o' and s[n+2]=='b':
        count=count+1
    n+=1
            
print('Number of times bob occurs is: ', count)