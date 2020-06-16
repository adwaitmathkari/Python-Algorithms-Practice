
def swap_all_odd_and_even_bits(n):
    rep='{:032b}'.format(n)
    newRep=''

    for i in range(0,32,2):        
        newRep+= rep[i+1] + rep[i]
    
    return int(newRep,2)



ns=[22, 13]

for n in ns:

    print(swap_all_odd_and_even_bits(n))