# PS

"""
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30

"""

"""
strategy:
    choose the rectangle size:
        either the closest two nos whose product is A
        or maybe the narrowest rectangle
        
    make a dictionary-- emptyN of centers to send to gopher with initial value 9
    
    as the replied vertex comes, update dictionary by subtracting 1 from each of the nine surrounding vertices
    
    choose that vertex to send where the empty neighbours are maximum
    
"""
import sys
def interact(testcase):
    a=int(input())#a is the squares to be dug
    #considering a straight line of a//3+1 x 3 to be dug completely in order to get a squares
    # thus to dig a//3+1 centres
    if a<9:
        a=9#always one full3x3 is dug
    
    
    if a%3==0:
        n=a//3
    else:
        n=a//3+1#rectangle of nby3 is to be dug
    
    emptyN = [9]*(n+3)
    ready234=[False]*(n+2)
    ready= [[],[], ready234[:], ready234[:], ready234[:]]
    #to send, considering the rectangle
        #(2,2), (4,2),(2,1+n), (4,1+n)
        #thus the centres to ssend will be: (3,3) to (3,n)
        #the list that is to be made ignores zero index, and thus the m,n that will be the input would directly be sent t the list 
    #the list will be 0-n+2 thus size n+3 and the vertices to check as centres will be empty[3] to empty[n]
    #empty[1] empty[2] and empty[n+1], empty[n+2] will occasionally get subtracted but will not be considered
    
        
    count=0
    print("%d %d"%(3,3))
    sys.stdout.flush()
    while True:
        count+=1
#         if count>1000:
#             print("COUNT: %d"%count)
        x,y = map(int, input().split())
        #here gopher sent an error
        if (x,y)==(-1,-1):
#             print("ERROR")
            break
        #gopher sends done
        elif (x,y)==(0,0):
#             print("case %d DONE in %d iterations"%(testcase,count))
            break
        
        #gopher sends the readied vertice
        else:
            #if already ready then do not subtract anything from emptyN[centres]
            #if the sent vertice was readied ryt now then update the emptyN list
            if ready[x][y]!=True:
                #update ready array
                ready[x][y]=True
#                 print(x,y)
                
                # subtract one from all the centres that had this readied square
                for i in range(y-1,y+2):
                    emptyN[i]-=1
            
            #now ready to send the next centre around which gopher will dig
            #find the centre which has maximum no of empty cells to dig    
            _max=emptyN[3]
            toSend=3
            for i in range(3,n+1):
                if emptyN[i]>_max:
                    _max=emptyN[i]
                    toSend=i
#             print("emptyN",emptyN[3:n+1])
#             print("ready", ready[2], ready[3],ready[4])
            #send the vertex with 3,centre as the coordinates
            print("%d %d"%(3,toSend))            
            sys.stdout.flush()
    return

t=int(input())
for x in range(t):    
    interact(x)



"""
import sys

def solve(a, b):
  m = (a + b) // 2
  print(m)
  sys.stdout.flush()
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  _ = int(input())
  solve(a + 1, b)
  
  """
