import math
from TreeNode import *


def validateBinarySearchTree(root):
	ans = [True]
	prev = [-math.inf]

	def inorder(root):
		if not root:
			return
		inorder(root.left)
		# print(prev, ans)
		if root.val >= prev[0]:
			prev[0] = root.val
		else:
			ans[0] = False
		inorder(root.right)

	inorder(root)
	return ans[0]


t = TreeNode(10)
t.left = TreeNode(17)
t.right = TreeNode(12)
t.left.left = TreeNode(4)
t.left.right = TreeNode(8)
t.left.right.right = TreeNode(8)
t.right.left = TreeNode(11)
t.right.right = TreeNode(38)
print(validateBinarySearchTree(t))
