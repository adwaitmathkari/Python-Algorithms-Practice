
#LOGIC based on the fact that each cell must have equal chocochips which is equal to the totalnoofchocochips/noofpieces
#thus to group rows into a piece, the total no of chips that should be there are chipspercell*(noofverticalcuts+1) similarly for vertical rows
#thus there has to be a near unique cutting combination for any cake

#implementation
#rows list, columns list, if cake[i][j] is @ rows[i]+=1 and cols[j]+=1
#find total no of chocolate chips
#divide by h+1, divide by v+1
#divide by h+1 and v+1
#decide placement for the horiz lines according to rows[]
#decide for vertical lines
#list hcuts[], vcuts[]
#simple for loop hcuts[i] to hcuts[i+1] and loop over vcuts and compare to the nchips/(h+1)/(v+1)


t=int(input())
for x in range(1,t+1):
    r,c,h,v=map(int, input().split())
    cake=[]

    for row in range(r):
        cake.append(input())
        
    #rows is the total no of chocochips per row and cols is that per column    
    rows=[0]*r
    cols=[0]*c
    chocochips=0
    
    #adding chips to rows cols and total
    for i in range(r):
        for j in range(c):
            if cake[i][j]=="@":
                rows[i]+=1
                cols[j]+=1
                chocochips+=1
    
    if chocochips==0:
        print("Case #%d: POSSIBLE"%x)
        continue
    
    if chocochips%((h+1)*(v+1))!=0:
        print("Case #%d: IMPOSSIBLE"%x)
        continue
    
    
    #chocochips per row col cell
    cperCell=chocochips/(h+1)/(v+1)
    cperRow=chocochips/(h+1)
    cperCol=chocochips/(v+1)
    
    
    
    #hcuts
    #-1 added as there is a cut at the start
    hcuts=[-1,]
    rowClubSum=0
    for i in range(len(rows)):
        rowClubSum+=rows[i]
        if rowClubSum==cperRow:
            hcuts.append(i)
            rowClubSum=0
    
    
    #vcuts
    vcuts=[-1,]
    colClubSum=0
    for i in range(len(cols)):
        colClubSum+=cols[i]
        if colClubSum==cperCol:
            vcuts.append(i)
            colClubSum=0

#     print(hcuts, vcuts, cperCell,cperRow,cperCol)
    
    
    #assert that there are h horiz and v vertical cuts
    if len(hcuts)!=h+2 or len(vcuts)!=v+2:
        print("Case #%d: IMPOSSIBLE"%x)
        continue
    
    chipsUnmatched=False
    for i in range(h+1):
        if chipsUnmatched:
            break
        for j in range(v+1):
            chips=0
            for k in range(hcuts[i]+1, hcuts[i+1]+1):
                for l in range(vcuts[j]+1, vcuts[j+1]+1):
                    if cake[k][l]=="@":
                        chips+=1
            if chips!=cperCell:
                print("Case #%d: IMPOSSIBLE"%x)
                chipsUnmatched=True
                break
           
    if not chipsUnmatched:               
        print("Case #%d: POSSIBLE"%x)
    
    
    
    
        
        
        
#case 1
#r,c<=10
#h=v=1
#brute force
#indexh can go from 0 to 8 after 0, after 1, after 2, after 3 ...
#lessequal is one piece and greater is other
#same for vertical

# 
# def bruteForceMethodForCase1ofProb():
#     
#     def equalDistribution(cake,i,j):
#         p=[0,0,0,0]
#         for t in range(len(cake)):
#             for u in range(len(cake[0])):
#                 if cake[t][u]=="@":
#                     if t<=i and u<=j:
#                         p[0]+=1
#                     elif t<=i and u>j:
#                         p[1]+=1
#                     elif t>i and u<=j:
#                         p[2]+=1
#                     else:
#                         p[3]+=1
#         return p[0]==p[1]==p[2]==p[3]        
#      
#     t=int(input())
#     for x in range(1,t+1):
#         r,c,h,v=map(int, input().split())
#         cake=[]
#         for row in range(r):
#             cake.append(input())
#          
#         possible=False
#         for indexh in range(9):
#             if possible:
#                 break
#             for indexv in range(9):
#                 if equalDistribution(cake, indexh,indexv):
#                     print("Case #%d: POSSIBLE"%x)
#                     possible=True
#                     break
#         if not possible:
#             print("Case #%d: IMPOSSIBLE"%x)
#      
 


   
    
    
    
    
    

