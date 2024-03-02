"""94-inordertraversal
进入循环，只要栈不为空，就执行以下操作：

a. 从栈顶弹出一个元组，得到命令和节点。
b. 如果命令为0，则将节点的值添加到结果列表 res 中。
c. 如果命令为1，则首先检查节点的右子节点是否存在，如果存在，
则将右子节点和命令1压入栈中。然后将当前节点和命令0压入栈中。
最后检查左子节点是否存在，如果存在，则将左子节点和命令1压入栈中。

"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def inorderTraversal(self,root):
        if not root:
            return []
        stack=[(1,root)]
        res=[]
        while stack:
            command,node=stack.pop()
            if command==0:
                res.append(node.val)
            else:
                if node.right:
                    stack.append((1,node.right))
                stack.append((0,node))
                if node.left:
                    stack.append((1,node.left))
        return res

if __name__ == "__main__":
    # 构建二叉树
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # 创建解决方案对象
    solution = Solution()

    # 进行中序遍历并打印结果
    print("Inorder Traversal:", solution.inorderTraversal(root))

class Solution:
    def inorderTraversal(self,root):
        res=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            res.append(root.val)
            root=root.right
        return res