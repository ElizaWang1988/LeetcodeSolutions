"""144-preorderTraversal
二叉树前序遍历"""

class TreeNode:
   def __init__(self,x):
       self.val=x
       self.left=None
       self.right=None

class Solution:
    def preorderTraversal(self,root):
        if not root:
            return []
        stack,res=[root,],[]
        while stack:
            root =stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res
