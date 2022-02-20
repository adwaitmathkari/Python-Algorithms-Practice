
from TreeNode import *
# Given a sorted (increasing order) array with unique integer 
# elements, write an algorithm to create a binary search tree 
# with minimal height and return the head of that tree. 
# The driver function will output the height of the tree.
# If it is not a valid BST output will be -1


def minimalTree(arr):
    #easy recursion
    # print(arr)
    n = len(arr)
    if n==1:
        return TreeNode(arr[0])
    if n==0:
        return None

    root = TreeNode(arr[n//2])

    root.left = minimalTree(arr[:n//2])
    root.right = minimalTree(arr[n//2+1:])

    return root


t = minimalTree(range(1,32))
printBST(t)
printInorder(t)
print(heightOfBST(t))

