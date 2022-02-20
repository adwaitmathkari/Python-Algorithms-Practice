from doublyLinkedList_crio import ListNode

def rotate_list_by_k(head, k):
    if not head:
        return head
    curr1=head
    c1 = 0
    while curr1:
        c1+=1
        curr1=curr1.next
    k = k%c1
    k=c1-k

    curr = head
    prev = None
    count = 1 
    newHead = head
    broken = False
    while curr:
        if count == k:
            prev = curr
            curr = curr.next
            newHead = curr
            prev.next = None
            count +=1
            broken =True
            if not curr:
                broken = False
                newHead = head
        else:
            count +=1
            prev = curr
            curr = curr.next
        if not curr:
            if count <= k:
                curr = head
    if broken:
        prev.next = head
    return newHead


for j in range(15):
    print(j,': ', end='')
    head = ListNode(0)
    tail = head
    for i in []:
        tail.next = ListNode(i)
        tail = tail.next
    head = head.next
    head = rotate_list_by_k(head, j)
    curr = head
    while curr:
        print(curr.val, end = '->')
        curr = curr.next
    print()
