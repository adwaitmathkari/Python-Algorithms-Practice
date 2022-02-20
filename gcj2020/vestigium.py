
t=int(input())

for case in range(1,t+1):
    n=int(input())

    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))

    rows,cols,trace = 0,0,0

    for i in range(n):
        check=[0]*(n+1)
        check2=[0]*(n+1)

        for j in range(n):
            if check[mat[i][j]]==1:
                rows +=1
                break
            else:
                check[mat[i][j]]=1
            
        
        for j in range(n):
            if check2[mat[j][i]]==1:
                cols +=1
                break
            else:
                check2[mat[j][i]]=1

        trace+=mat[i][i]

    print("Case #"+ str(case) +": "+str(trace)+ " " + str(cols)+ " " +str(rows))






