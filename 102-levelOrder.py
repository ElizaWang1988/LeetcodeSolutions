"""102-levelOrder

"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val  
        self.left=left
        self.right=right

class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        currentStack=[root]
        outList=[]
        while currentStack:
            nextStack=[]
            for point in currentStack:
                if point.left:
                    nextStack.append(point.left)
                if point.right:
                    nextStack.append(point.right)
                outList(point.val)
                currentStack=nextStack
            return outList
 
#  # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         currentStack=[root]
#         outList=[]
#         while currentStack:
#             nextStack=[]
#             outstring=[]
#             for point in currentStack:          
#                 if point.left:
#                   nextStack.append(point.left)
#                 if point.right:
#                   nextStack.append(point.right)
#                 outstring.append(point.val)
#             outList.append(outstring)
#             currentStack=nextStack
#         return outList

   