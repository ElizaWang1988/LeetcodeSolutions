"""234 isPalindrome
https://blog.csdn.net/qq_34364995/article/details/80640449
"""
# class Solution:
#     def isPalindrome(self,head):
#         if not head or not head.next:
#             return True
#         l=[]
#         p=head
#         while p.next:
#             l.append(p.val)
#             p=p.next
#         l.append(p.val) #最后一个点没有加进去，要加进去
#         return l==l[::-1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:#这里快指针的判读条件跟判断环形有一点不同
            fast = fast.next.next
            slow = slow.next
        def reverse_list(head):
            if head is None:
                return head
            cur = head
            pre = None
            while cur:
                tmp =cur.next
                cur.next= pre
                pre = cur
                cur = tmp         
            return pre
        p = reverse_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p.val == q.val


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# 创建一个回文链表：1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

# 打印链表
print("Original linked list:")
print_list(head)

# 创建一个Solution对象
sol = Solution()

# 调用isPalindrome函数判断链表是否为回文
result = sol.isPalindrome(head)

# 输出结果
print("Is Palindrome:", result)

