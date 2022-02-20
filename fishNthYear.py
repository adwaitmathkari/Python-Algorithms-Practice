# fishNthYear

# Problem Description
# You need to find the number of fish there will be at a year N, given the initial number NB of fish at year 0. To simplify things, there are no males and females: every fish gives birth to G fish per year.

# But be careful, because:

# Fish only give birth during the first R years of their lives

# Fish only live L years (initial fish are dead at year L)

# Input format
# N NB G L R

# Output format
# Number of fish in year N



def population(n, nb, g, l, r):
    
    if n==0:
        if l>0:
            return nb
        return 0

    if r<=0:
        
        return population(n-1, nb, g, l-1, r-1)
        
    else:
        return population(n-1, nb, g, l-1, r-1) + population(n-1, nb*g, g, l,r)
    


print(population(3,2,2,4,2))
print(population(1,2,1,4,2))



