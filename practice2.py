# Sorting practice
from typing import List
import random

#bubble sort

def bubbleSort(l):
    # bubble sort is where you go on comparing adjacent elements 
    # the iteration when there is no swap means that the list is sorted

    ln=len(l)
    it=0
    sw=1
    while(sw != 0):
        # print(l)
        it+=1
        sw=0
        for i in range(ln-1):
            if l[i]>l[i+1]:
                swap(l,i,i+1)
                sw=1
    
    
    # print('iterations:', it)

def swap(l, i1, i2):
    temp=l[i2]
    l[i2]=l[i1]
    l[i1]=temp



def testSort():
        
    l=[1,2,234,15,90,12,23,4,6,7,1,4,901]
    l2=[1,-1]
    l3=[random.randint(-10000,10000) for i in range(200)]

    # f=bubbleSort
    # f=insertionSort
    f=selectionSort

    f(l)
    f(l2)
    f(l3)


    print(l)
    print(l2)
    print(l3)
    




# insertion sort goes like the foll
# take the next ele and insert it into the preceding sorted array
# thus first ele remainsin place
# next the second ele should be inserted the preceding sorted array 
# the n th tele should be inserted into the sorted array of n-1 elements 
# thus swap it till you find a smaller ele 

#choose each successive indexed element and insert it into the preceding array

def insertionSort(l):
    ln=len(l)
    for i in range(ln):
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                swap(l,j,j-1)
            else:
                break

        

# select the min from the unplaced elements and place it
def selectionSort(l):
    ln=len(l)
    for i in range(ln):
        min_=l[i]
        min__=i
        for j in range(i,ln):
            if l[j]<min_:
                min_=l[j]
                min__=j
        swap(l,i,min__)


# quick sort


def quickSort(l):
    
    pass



def bubbleSort(l):
    pass


testSort()
