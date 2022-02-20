def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    ans=()
    for i in range(len(aTup)):
        if i%2==0:
            ans=ans+aTup[i:i+1]
    return ans