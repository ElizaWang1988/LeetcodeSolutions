"""328-奇偶链表
https://blog.csdn.net/xiaoyue_/article/details/124611725
"""
# class Solution:
#     def oddEvenList(self, head):
#         if not head or not head.next:
#             return head
#         even_head=head.next
#         odd,even=head,head.next
#         while odd.next and even.next: #pay attetion to the conditions for the end of the loop (the critical value)
#             odd.next=even.next
#             odd=odd.next
#             even.next=odd.next
#             even=even.next
#         odd.next=even_head
#         return head
       
class ListNode(object):
   def __init__(self,val,next=None):
      self.val=val
      self.next=next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
          return head
        odd_p=head
        even_head,even_p=head.next,head.next
        p=head.next.next
        i=3
        while p:
           nxt=p.next
           if i%2==1:
              odd_p.next=p
              odd_p=odd_p.next
           else:
              even_p.next=p
              even_p=even_p.next
           i+=1
           p=nxt
        even_p.next=None
        odd_p.next=even_head
        return head

              

# 创建链表 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# 创建 Solution 类的实例
sol = Solution()

# 打印原始链表
print("原始链表：", end=" ")
current = node1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# 调用 oddEvenList 方法
result_head = sol.oddEvenList(node1)

#打印修改后的链表
print("修改后的链表：", end=" ")
current = result_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

   