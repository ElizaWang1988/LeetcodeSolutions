"""145-postorderTraversal
https://cloud.tencent.com/developer/article/1629239
"""
class Solution:
    def postorderTraversal(self,root):
        if not root:
            return []

        stack,res=[root,],[] 
        while stack:
            root=stack.pop()
            res.append(root.val)
            if  root.left:
                stack.append(root.left)
            if  root.right:
                stack.append(root.right)
        return res[::-1]
#acgfbed
#de
            
