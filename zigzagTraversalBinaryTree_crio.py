

# Definition of TreeNode
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


# Given a binary tree, return the zigzag level order traversal of its nodes'
# values.
# (i.e. from left to right, then right to left for the next level and alternate
# for every level).


def zigzagLevelOrder(root):
    level = 0
    stack = [root]
    final = [[root.val]]
    level += 1

    while stack != []:
        subFinal = []
        newStack = []
        while stack != []:
            node = stack.pop()
            if level % 2 == 1:
                if node.right:
                    subFinal.append(node.right.val)
                    newStack.append(node.right)
                if node.left:
                    subFinal.append(node.left.val)
                    newStack.append(node.left)
            else:
                if node.left:
                    subFinal.append(node.left.val)
                    newStack.append(node.left)
                if node.right:
                    subFinal.append(node.right.val)
                    newStack.append(node.right)
        stack = newStack
        level += 1
        final.append(subFinal)

    return final


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)
a.right.right.left = TreeNode(14)
a.right.right.right = TreeNode(15)
a.left.right.left = TreeNode(10)
a.left.right.right = TreeNode(11)

print(zigzagLevelOrder(a))