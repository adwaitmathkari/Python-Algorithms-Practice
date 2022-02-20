from ListNode import *


# Complete the following funtion
def deleteUnvisitedNodes(head):
    if not head:
        return head
    curr = head
    while True:
        node = getNext(curr, curr.val)
        if not node:
            curr.next = None 
            break
        curr.next = node
        curr = node
    return head

    
    
def getNext(node, k):
    for i in range(k):
        if not node:
            return None
        node = node.next
    return node
        
head = createList([])
print(extractList(deleteUnvisitedNodes(head)))
