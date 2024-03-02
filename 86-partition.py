# """
# 86-partition
# """
# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class Solution:
#     def partition(self,head:ListNode,x:int)->ListNode:

#         small_node=ListNode(-2)
#         large_node=ListNode(-1)
#         cur=head
#         curs,curl=small_node,large_node
#         while cur is not None:
#             if cur.val<x:
#                 curs.next=ListNode(cur.val)
#                 curs=curs.next
#             else:
#                 curl.next=ListNode(cur.val)
#                 curl=curl.next

#             cur=cur.next
#         curs.next=large_node.next
#         return small_node.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个哑结点用于连接小于 x 和大于等于 x 的节点
        dummy_small = ListNode(0)
        dummy_large = ListNode(0)
        # 创建两个指针分别指向哑结点
        small_ptr = dummy_small
        large_ptr = dummy_large
        
        # 遍历原链表
        while head:
            # 如果当前节点值小于 x，则连接到小于 x 的链表
            if head.val < x:
                small_ptr.next = head
                small_ptr = small_ptr.next
            # 如果当前节点值大于等于 x，则连接到大于等于 x 的链表
            else:
                large_ptr.next = head
                large_ptr = large_ptr.next
            # 移动原链表指针
            head = head.next
        
        # 将大于等于 x 的链表连接到小于 x 的链表后面
        small_ptr.next = dummy_large.next
        # 将大于等于 x 的链表尾部置为 None，防止出现循环
        """我的理解是，原始链表不是按顺序遍历的吗，比x大的节点，
        不是基本按照原始链表从前往后的顺序，加到新链表里面了吗，
        只能是最后一个比x大的节点，后面可能还接着一个比x小的节点，
        因此如果不把最后一个节点的next指向set为none，会变成循环递归"""
        large_ptr.next = None
        
        # 返回新的链表头部
        return dummy_small.next

#         """
# 86-partition
# """
# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class Solution:
#     def partition(self,head:ListNode,x:int)->ListNode:

#         small_node=ListNode(0)
#         large_node=ListNode(0)
#         cur=head
#         curs,curl=small_node,large_node
#         while cur is not None:
#             if cur.val<x:
#                 curs.next=cur
#                 curs=curs.next
#             else:
#                 curl.next=cur
#                 curl=curl.next

#             cur=cur.next
#         curs.next=large_node.next
#         curl.next=None
#         return small_node.next
