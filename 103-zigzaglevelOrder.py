
"""103-zigzaglevelOrder"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        outList=[]
        currentStack=[root]
        i=1
        while currentStack:
            nextStack=[]
            outstring=[]
            for point in currentStack:
                if point.left:
                    nextStack.append(point.left)
                if point.right:
                    nextStack.append(point.right)
                outstring.append(point.val)
            currentStack=nextStack
            if i%2==1:
                outList.append(outstring)
            if i%2==0:
                outList.append(outstring[::-1])
            i=i+1
        return outList
                
           
        


