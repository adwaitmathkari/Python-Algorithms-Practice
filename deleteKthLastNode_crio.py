from ListNode import ListNode, createList, extractList

'''
# Definition for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
def delete_kth_to_last(head, k):
    if k==0:
        return head
    count = 0
    c = head
    kPointer = head
    while c:
        count +=1
        if count > k+1:
            c=c.next
            kPointer = kPointer.next
        else:
            c=c.next
    
    if count == k:
        return head.next
    if k>count:
        return head
    
    kPointer.next = kPointer.next.next
    return head


def move_middle_to_head(head):
    
    prev = None
    slow = head
    fast = head.next if head else None
    if not fast or not slow:
        return head
    
    while (fast):
        prev =slow
        slow = slow.next
        fast = fast.next.next if fast.next else fast.next
    
    prev.next = slow.next
    slow.next = head
    
    
    return slow

arr1 = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1], [1,2], [1,2,3], [], [1,2,3,4,5,6], [1,2,3,4,5,6,7]]


for arr in arr1:    
    head = createList(arr)
    head = move_middle_to_head(head)
    print( extractList(head))

