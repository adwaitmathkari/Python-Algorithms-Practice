

# Definition of TreeNode
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

# A function to do inorder tree traversal 

def printInorder(root):
    def printInorder1(root): 
    
        if root: 
    
            # First recur on left child 
            printInorder1(root.left) 
    
            # then print the data of node 
            print(root.val,  end=' '), 
    
            # now recur on right child 
            printInorder1(root.right) 
    printInorder1(root)
    print()
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val, end=' '), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val, end=' '), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 


def heightOfBST(root):
    def traverse(root, h, maxh):
        if not root:
            if h>maxh[0]:
                maxh[0] = h
            return
        h+=1
        traverse(root.left, h, maxh)
        traverse(root.right, h, maxh)
    maxh = [0]
    traverse(root, 0, maxh)
    return maxh[0]


def printBST(root):
    currl = [root]
    nextl = []
    flag = True

    while flag:
        print([i.val if i else None for i in currl ])
        nextl= []
        for i in currl:
            if i:
                nextl+= [i.left, i.right]
            else:
                nextl+= [None, None]
        currl = nextl
        flag = False
        for i in currl:
            if i:
                flag = True
    