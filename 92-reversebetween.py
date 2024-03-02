# class ListNode:():
#     def _init_(self,val,next=None):
#         self.val=val
#         self.next=next
# class Solution(object):
#     def reverBetween(self,head:ListNode,m,n):
#         if not head or not head.next or m==n:
#             return head
#         dummy=ListNode(0)
#         dummy.next=head
#         start=dummy
#         for i in range(m-1):
#             start=start.next
        
#         end=cur=start.next
#         p=None
#         for i in range(n-m+1):
#             temp=cur.next
#             cur.next=p
#             p=cur
#             cur=temp
#         start.next=p
#         end.next=cur 
"""https://www.jianshu.com/p/91b050e076b4"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or not head.next or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for i in range(left-1):
            start = start.next
        cur = end = start.next
        p = None
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = p
            p = cur
            cur = tmp
        start.next = p
        end.next = cur
        return dummy.next

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# 创建测试链表：1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 创建 Solution 实例
sol = Solution()

# 测试 reverseBetween 方法
left = 2
right = 4
new_head = sol.reverseBetween(head, left, right)

# 打印翻转后的链表
printLinkedList(new_head)
