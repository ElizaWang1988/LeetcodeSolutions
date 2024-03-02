"""114-flatten
https://blog.csdn.net/qq_43593534/article/details/124008682
https://juejin.cn/post/6856349605895307272"""
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def flatten(self,root):
        if not root:
            return []
        while root:
            if root.left:
                temp=root.right
                root.right=root.left
                root.left=None
                h=root.right      #finding the last right node of the left tree 
                while h.right:
                    h=h.right
                h.right=temp
            root=root.right

