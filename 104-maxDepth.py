"""104-maxDepth"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
#递归
# class Solution:
#     def maxDepth(self,root):
#         def max_depth(root):
#             if not root:
#                 return 0
#             max_left=max_depth(root.left)
#             max_right=max_depth(root.right)
#             return max(max_left,max_right)+1
#         return max_depth(root)
#迭代
class Solution:
    def maxDepth(self,root):
        stack=[]
        if root:
            stack.append((root,1))
        max_depth=0
        while stack:
            tree_node,cur_depth=stack.pop()
            if tree_node:
                max_depth=max(max_depth,cur_depth)
                stack.append((tree_node.left,cur_depth+1))
                stack.append((tree_node.right,cur_depth+1))
        return max_depth

if __name__ == "__main__":
    # 构建一个二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # 创建 Solution 类的实例
    solution = Solution()
    # 调用 maxDepth 方法计算二叉树的最大深度
    depth = solution.maxDepth(root)
    print("二叉树的最大深度为:", depth)
