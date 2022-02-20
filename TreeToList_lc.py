# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         #serialize a binary tree
        
#         # 12nn34nn5
#         # recursion on the same string 
#         l=[]
#         def addToL(node):
#             if node==None:
#                 l.append('n')
#             else:
#                 l.append(node.val)
#                 addToL(node.left)
#                 addToL(node.right)
#         addToL(root)
#         return l
        
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         i=0
#         node=TreeNode(data[i])
#         i+=1
#         def addToTree(node):
#             if data[i] != None:
#                 newNode=TreeNode(data[i])
#                 node.left=newNode
#                 i+=1
#                 addToTree(newNode)
#                 newNode2=TreeNode(data[i])
#                 node.right=newNode2
#                 addToTree(newNode2)
#         addToTree(node)
#         return node
                
            
            
            
            
            
# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.deserialize(codec.serialize(root))




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #serialize a binary tree
        
        # [1,2,None,None,3,4,None,None,5]
        # recursion on the same string 
        l=[]
        def addToL(node):
            if node==None:
                l.append(None)
            else:
                l.append(node.val)
                addToL(node.left)
                addToL(node.right)
        addToL(root)
        return l
        
        

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i=[0]
        node=TreeNode(data[i[0]])
        i[0]+=1
        def addToTree(node):
            # print(i[0])
            if  data[i[0]] != None:
                newNode=TreeNode(data[i[0]])
                node.left=newNode
                i[0]+=1
                if i[0]==len(data):
                    return
                addToTree(newNode)
                newNode2=TreeNode(data[i[0]])
                node.right=newNode2
                i[0]+=1
                if i[0]==len(data):
                    return
                addToTree(newNode2)
        addToTree(node)
        return node
                
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(100)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)

c=Codec()

l=c.serialize(root)
node1=c.deserialize(l)
print(l)

print(node1.val)
print(root.left.val)
print(root.left.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)


