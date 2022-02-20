
def CountNodes (Val, v, N, Q, u, V, X):
    # Write your code here
    # val is an array
    # u are the parent nodes v are the child nodes and there is 1-1 correspondence
    #V is array of query vertices and X is corresponding comparison values i.e count of nodes <=Xi
    # print(Val)
    Val=list(Val)
    tree=[None]*(N+1)
    tree[1]=1
    for i in range(N-1):
        tree[v[i]]=u[i]
    # print(tree)   
    out_=[]
    for i in range(Q):
        #V[i] is the node 
        node=V[i]
        cx=X[i]
        count=0
        while node!=1:
            if Val[node-1]<=cx:
                count+=1
            node=tree[node]
        if Val[0]<=cx:
            count+=1
        out_.append(count)
    
    return out_
    
    
    

N, Q = map(int, input().split())
Val = list(map(int, input().split()))
u, v = [], []
for i in range(0, N - 1):
    tu, tv = map(int, input().split())
    u.append(tu)
    v.append(tv)
V, X = [], []
for i in range(Q):
    tV, tX = map(int, input().split())
    V.append(tV)
    X.append(tX)

out_ = CountNodes(Val, v, N, Q, u, V, X)
print('\n'.join(map(str, out_)))