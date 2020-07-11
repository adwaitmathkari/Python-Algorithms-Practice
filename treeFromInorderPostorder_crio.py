from TreeNode import *

def buildTree(preorder, inorder):
    if inorder == []:
        return None
    root = TreeNode(preorder[0])
    rootI = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:1+rootI], inorder[:rootI])
    root.right = buildTree(preorder[1+rootI:], inorder[rootI+1:])
    return root

root = buildTree([1,2,4,5,3], [4,2,5,1,3])
printPreorder(root)
print()
printInorder(root)
print()