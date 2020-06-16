from ListNode import *



def print_list(head):
    # a=0
    # while a<40 and head:
    #     print(head.val, end='->')
    #     head = head.next
    #     a+=1
    # print('null')
    l = extractList(head)
    print(len(l))
    print(*l)


# TODO: CRIO_TASK_MODULE_LINKED_LIST_ODD_EVEN_SPLIT
# Input:
#      1. head of linked list
# Task:
#      1. if linked list has no loop just split odd position and even position elements
#      2. if linked list has loop then return all odd position elements in the loop
#          and even positions elements in the loop
#  Output:
#      1. head of linked list of all nodes in odd positions
#      2. head of linked list of all nodes in even positions



# python3 runner.py --problem LinkedListRandomReversal --lang python --run


###returns a linked list split into two lists by odd even
def split_linear_list_odd_even(head):


    # this looks easy
    # head, and alternate elements go to two different lists like get appended to 2 different tails
    # right?
    # if this were an important problem to solve the nwhat would I do?
    # try to solv eby brute ofrce
    # try to solve methodically
    # write down soln step by step and the ncheck whether its right or not

    #put first node in first list
    # put next node in next list
    # keep tab on m and null next ele

    headOdd = ListNode(None)
    tailOdd = headOdd
    headEven = ListNode(None)
    tailEven = headEven

    curr = head
    index = 1
    while True:
        if not curr:
            break
        temp = curr.next
        # if nNodes>m:
        #     break
        if index % 2 == 1:
            tailOdd.next = curr
            curr.next = None
            tailOdd = curr
        else:
            tailEven.next = curr
            curr.next = None
            tailEven = curr
        index+=1
        curr = temp
    headOdd, headEven = headOdd.next, headEven.next
    if headOdd.val == "added":
        headOdd = headOdd.next

    return headOdd, headEven

##finds a cycle in a linked list and returns the steps taken to reach the common node in a floyds two pointer approach
def floyds_2pointer_steps(head) -> (int, ListNode):
    # return the no of steps taken by the slower pointer to reach a common node
    # and return the common node where the 2 pointers meet 
    # if the list is not cyclic then returns -1
    
    if not head:
        return -1, None
    #pointer
    p1 = head
    p2 = head.next
    steps = 1
    if p2 == None:
        return -1,None

    while(True):
        if p1 == p2:
            return steps, p1
        p1=p1.next
        
        p2 = p2.next
        if p2==None:
            return -1,None
        p2=p2.next
        if p2 == None:
            return -1,None
        steps+=1

    
## if cyclic -> returns linear list 
#               head at the point of repetition  
## if linear-> returns as it is 
def return_linear_list(head):
    ## find if cyclic or not
    tup1 = floyds_2pointer_steps(head)
    if tup1[0] == -1:
        return head

    tup2 = floyds_2pointer_steps(tup1[1])
    ##find the no of nodes in cycle
    nNodesInCycle = tup2[0]
    

    ##find the point of repetition
    p1 = head
    p2= head
    count = 1
    while True:
        if p2.next == p1:
            p2.next = None
            if (count-nNodesInCycle)%2 == 1:
                n = ListNode('added')
                n.next = p1
                return n
            else:
                return p1
        if count<nNodesInCycle:
            p2=p2.next
        else:
            p1=p1.next
            p2 = p2.next
        count+=1
        


def split_list_by_odd_or_even(head):
    
    head = return_linear_list(head) 


    return split_linear_list_odd_even(head)



def test(arr,cylicIndex):
    head1= generateLinkedListWithCycle(arr,cylicIndex)

    # print_list(head1)
    print('----------final lists -------------------')
    finLists = split_list_by_odd_or_even(head1)
    print_list(finLists[0])
    # print()
    print_list(finLists[1])

arr = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [1,2,-1,-2,-3,-4,-5,-6,-7], [1,2,3,4,5,6,7,8,9,0,10,10,10,20,30,40,50,60],[1,2,3,4,5,6,7,8], [0,0,1, 2,2,3,7,8,9]]
for inp in arr[:1]:
    pass
# for i in range(-1,5):

#     test([1,2,3,4,5],i)
test([1,2,3,4,5], 3)

    # print(a[0])
    # lists = split_list_by_odd_or_even(createList(inp))

    # print("odd", *extractList(lists[0]), "even", *extractList(lists[1]))


# head1 = generateLinkedListWithCycle(arr[0],1)
# print_list(head1)
# # a= floyds_2pointer_steps(head1)
# # print(a[0])
# # print(floyds_2pointer_steps(a[1])[0])
# # print("--------------linear list------------------")
# # print_list(return_linear_list(head1))

# print('----------final lists -------------------')
# finLists = split_list_by_odd_or_even(head1)
# print_list(finLists[0])
# print()
# print_list(finLists[1])

# # finding a loop in a linked list
# # 2 pointer approach

