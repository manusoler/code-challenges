class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        """
        1. If tree is empty then return 0
        2. Else
            (a) Get the max depth of left subtree recursively  i.e., 
                call maxDepth( tree->left-subtree)
            (a) Get the max depth of right subtree recursively  i.e., 
                call maxDepth( tree->right-subtree)
            (c) Get the max of max depths of left and right 
                subtrees and add 1 to it for the current node.
                max_depth = max(max dept of left subtree,  
                                    max depth of right subtree) 
                                    + 1
            (d) Return max_depth
        """
        if root == None:
            return -1
        else:
            max_left = self.getHeight(root.left)
            max_right = self.getHeight(root.right)
            return max([max_left, max_right]) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)