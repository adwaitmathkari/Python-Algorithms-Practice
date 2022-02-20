from ListNode import ListNode, extractList
from ListNode import createList as createLinkedList
import time
class Solution:

    def print_list(self, head):
        print("List : ", end=' ')

        while head:
            print(head.val, end=' ')
            head = head.next

        print()

    # TODO: CRIO_TASK_MODULE_LINKED_LIST_RANDOM_REVERSAL
    # Input:
    #      1. singly linked list
    #      2. list of numbers
    #
    # Task:
    #      for every `k` in numbers
    #          reverse next k elements of the linked list (for first k start from head)
    #          append the reversed list to result linked list
    #
    # Output:
    #      Return the result list

    def performRandomReversal(self, head, nums):

        # 1,2,3,4,5,6,7,8,9
        # 3 1 3

        # reversee the list for each num
        curr = head

        # 1,2,3,4,5,6,7,8,9
        # 3 1 3

        # reversee the list for each num

        #newlist

        # start by keeping 2 pointers headFinal and tailFinal
        # these will monitor the position of the head and tail of the final linked list
        # tailFinal will be useful to append the next head of a reversed sublinked list.
        # the headFinal will be returned
        # so the new list will start from headFinal and end at tailFinal


        # going over the list once through curr. O(n)
        # reversing at eac step,
        # if starting at a num then the that curr is going to be the tail of this reversed list
        # i.e. this is the first element right now that means it will be the last element after the list is reversed
        # so going on for i in range(num)
        # reversing the list and finally, attach tailFinal.next = subHead. \
        # this subHead is actually the last element in the for loop of length num
        # this will terminate when curr is null
        # at each next iteration of the for loop, curr is incremented
        # at each next iteration of the nums loop, the previous list is attached to the tailFinal and after that,
        # a new reversed sublist will start to get created to be added further to tailFinal
        # also, tailFinal will be set at the tail of the newly added sublist

        # iterating over nums
        # for each num, a new reversed sublist is created
        # and finally it is appended to the tailFinal


        headFinal = ListNode(None)
        tailFinal = headFinal

        for num in nums:
            if not curr:
                break
            if num==0:
                continue

            # set the tail and the head as this is the first element of the sublist
            # for each sublist that needs to be reversed,
            # in first iteration set head and tail
            # and then hit awhile loop 
            temp = curr.next
            head2 = curr
            head2.next = None
            tail2 = head2
            count = 1
            curr = temp
            # while loop to reverse the num number of elements of the list
            while count < num:
                if not curr:
                    break

                temp = curr.next
                curr.next = head2
                head2 = curr
                curr = temp

                count += 1

            # after the while loop ends, attach the newly reversed sublist to the finalList
            # ie to tailFinal
            tailFinal.next = head2
            tailFinal = tail2

        # if the sum of nums is less thanno of elements of the arr then append the remaining in the end
        if curr is not None:
            tailFinal.next = curr

        # headfinal.next is returned since a null node was added as head earlier
        return headFinal.next



    # def performRandomReversal2(self, head, nums):

    #         # 1,2,3,4,5,6,7,8,9
    #         # 3 1 3 

    #         # reversee the list for each num
            

    #         #newlist

    #         # start by keeping 2 pointers headFinal and tailFinal
    #         # these will monitor the position of the head and tail of the final linked list
    #         # tailFinal will be useful to append the next head of a reversed sublinked list.
    #         # the headFinal will be returned
    #         # so the new list will start from headFinal and end at tailFinal
            
    #         headFinal = None
    #         tailFinal = None

    #         # going over the list once through curr. O(n)
    #         # reversing at eac step, 
    #         # if starting at a num then the that curr is going to be the tail of this reversed list 
    #         # i.e. this is the first element right now that means it will be the last element after the list is reversed
    #         # so going on for i in range(num)
    #         # reversing the list and finally, attach tailFinal.next = subHead. \
    #         # this subHead is actually the last element in the for loop of length num
    #         # this will terminate when curr is null
    #         # at each next iteration of the for loop, curr is incremented
    #         # at each next iteration of the nums loop, the previous list is attached to the tailFinal and after that, 
    #         # a new reversed sublist will start to get created to be added further to tailFinal
    #         # also, tailFinal will be set at the tail of the newly added sublist
            
    #         curr = head

    #         # iterating over nums
    #         # for each num, a new reversed sublist is created
    #         # and finally it is appended to the tailFinal 
    #         for num in nums:
    #             if not curr:
    #                 break
    #             if num==0:
    #                 continue
    #             # set the tail and the head as this is the first element of the sublist
    #             temp = curr.next
    #             head2 = curr
    #             head2.next = None
    #             tail2 = head2
    #             count = 1
    #             curr = temp
                
    #             while count<num:
    #                 if not curr:
    #                     break

    #                 temp = curr.next                                       
    #                 tempHead = head2
    #                 head2 = curr
    #                 head2.next = tempHead
    #                 count+=1

    #                 curr = temp
                
    #             if not headFinal:
    #                 headFinal = head2
    #                 tailFinal = tail2
    #             else:
    #                 tailFinal.next = head2
    #                 tailFinal = tail2


    #         if curr is not None:
    #             tailFinal.next = curr

    #         return headFinal

# 5
# 1 2 3 4 5
# 2
# 2 2

s=Solution()

head1 = createLinkedList([i for i in range(100)])
# print("Arr:", *extractList(head1))

arr2 = extractList(s.performRandomReversal(head1, [
                   10, 20, 18, 13, 14, 15, 16, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1000]))
# print("Sol:", *arr2)

f=open('./reverseLinkedList_tests/perf-input-5.txt', 'r')
# f=open('./reverseLinkedList_tests/perf-input-5.txt', 'r')
n=f.readline()
# print(f.readline().split(' ')[0:100])
arr3 = list(map(int,f.readline().split(' ')[:-1]))

n=f.readline()

sarr3=f.readline().split(' ')
# for i in range(len(sarr3)):
#     try:
#         sarr3


karr3 = list(map(int, sarr3))
f.close()

f=open('./reverseLinkedList_tests/perf-output-5.txt', 'r')
f.readline()
solArray = list(map(int,f.readline().split(' ')))
print(len(solArray))
t=time.time()

ansArr = extractList(s.performRandomReversal(createLinkedList(arr3), karr3))
print(len(ansArr))
print(time.time()-t)
for i in range(250000):
    if solArray[i] != ansArr[i]:
        print(solArray[i], ansArr[i])
        print('wrong at', i)

print(*solArray[-100:])
print(*ansArr[-100:])
assert(solArray == ansArr)
print(sum(karr3))

