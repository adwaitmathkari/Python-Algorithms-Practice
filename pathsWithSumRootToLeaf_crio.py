# Given a binary tree and a sum, find the number of root-to-leaf
# paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.

from TreeNode import *


def pathsWithSumRootToLeaf(root, k):
    countL = [0]
    pathSum(root, k, countL)
    return countL[0]


def pathSum(root, k, countL):
    if root == None:
        return
    if root.val  == k and root.left == None and root.right == None:
        countL[0] += 1
        return

    pathSum(root.left, k-root.val, countL)
    pathSum(root.right, k-root.val, countL)


t = TreeNode(10)
t.left = TreeNode(7)
t.right = TreeNode(12)
t.left.left = TreeNode(4)
t.left.right = TreeNode(8)
t.left.right.right= TreeNode(8)
t.right.left = TreeNode(11)
t.right.right = TreeNode(38)

print(pathsWithSumRootToLeaf(t, 33))
