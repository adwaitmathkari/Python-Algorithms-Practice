

class DoublyLinkedListNode:
    def __init__(self, x, p= None,n= None):
        self.val = x
        self.prev = p
        self.next = n


# Definition for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def doublyLinkedCircularList(head):

    curr = head
    prev = None
    headDouble = DoublyLinkedListNode(0)
    tailDouble = headDouble
    #new list


    while curr:
        newNode = DoublyLinkedListNode(curr.val, tailDouble, None)
        tailDouble.next = newNode
        tailDouble = newNode
        curr = curr.next
    
    headDouble = headDouble.next
    if headDouble:
        tailDouble.next = headDouble
        headDouble.prev = tailDouble
    
    return headDouble


def main():
        
    head = ListNode(0)
    tail = head
    for i in [1,2,3,4,5,6]:
        tail.next = ListNode(i)
        tail = tail.next

    hd = doublyLinkedCircularList(head)

    curr = hd
    for i in range(10):
        print(curr.val, end = '->')
        curr = curr.next
    print()
    # print('---------')
    curr = hd
    for i in range(10):
        print(curr.val, end = '->')
        curr = curr.prev


if __name__ == '__main__':
    main()