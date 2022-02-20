from ListNode import *

def connectedComponents(head, subset):
    # Write your code here
    curr = head
    prevInSubset = False
    comp = []
    final = []
    s=set()
    for i in subset:
        s.add(i)
    while curr:
        if curr.val not in s:
            if prevInSubset:
                comp[-1].next = None
                final.append(comp[0])
                comp = []
            prevInSubset = False
        else:
            comp.append(curr)
            prevInSubset = True
        curr = curr.next
    # print(final)
    # print(final[0].val)
    if comp!=[]:
        final.append(comp[0])
    return final


def main():
    lst = [2,1,18,2,3,4,10,2,3,5]    
    subset = [1,2,3,4,5,6,7,8,9]

    head = createList(lst)

    result = connectedComponents(head, subset)
    for componentHead in result:
        componentList = extractList(componentHead)
        print(*componentList)

if __name__ == '__main__':
    main()