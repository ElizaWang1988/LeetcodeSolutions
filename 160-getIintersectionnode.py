"""双指针法"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     """two """
#     def getIntersectionNode(self,headA,headB):
#         head1=headA
#         head2=headB
#         while head1!=head2:
#             print("head1:", head1.val if head1 else None)
#             print("head2:", head2.val if head2 else None)
#             head1=head1.next if head1 else headB
#             head2=head2.next if head2 else headA
#         return head1

# # 创建链表A: 1 -> 2 -> 3 -> 4 -> 5
# headA = ListNode(1)
# headA.next = ListNode(2)
# headA.next.next = ListNode(3)
# headA.next.next.next = ListNode(4)
# headA.next.next.next.next = ListNode(5)

# # 创建链表B: 6 -> 7 -> 8 -> 9 -> 10
# headB = ListNode(6)
# headB.next = ListNode(7)
# headB.next.next = ListNode(8)
# headB.next.next.next = ListNode(9)
# headB.next.next.next.next = ListNode(10)

# # 设置链表A和链表B的交叉点为节点3
# headA.next.next.next = headB.next.next
# # 输出链表B的所有数字
# # current = headA
# # while current:
# #     print(current.val, end=" ")
# #     current = current.next

# # 测试代码
# solution = Solution()
# intersection_node = solution.getIntersectionNode(headA, headB)

# if intersection_node:
#     print("Intersection node value:", intersection_node.val)
# else:
#     print("No intersection point.")

# class ListNode(self,val,next):
#    def _init_(self,val=0,next=None):
#      self.val=val
#      self.next=next

# class Solution(object):
#     def getIntersectionNode(self,headA,headB):
#         if not headA or not headB：
#            return None
#         tempA=headA
#         tempB=headB
#         listA=[]
#         listB=[]
#         while tempA is not None:
#             listA.append(tempA)
#             tempA=tempA.next
#         while tempB is not None:
#             listB.append(tempB)
#             tempB=tempB.next
#         if len(listA)>1 and len(listB)>1 and listA[-2]==listB[-2]:
#             listA.pop()
#             listB.pop()
#         if listA[-1]==listB[-1]:
#             return listB[-1]
#         else:
#             return None
# # 创建链表A: 1 -> 2 -> 3 -> 4 -> 5
# headA = ListNode(4)
# headA.next = ListNode(1)
# headA.next.next = ListNode(8)
# headA.next.next.next = ListNode(4)
# headA.next.next.next.next = ListNode(5)

# # 创建链表B: 6 -> 7 -> 8 -> 9 -> 10
# headB = ListNode(5)
# headB.next = ListNode(6)
# headB.next.next = ListNode(1)
# headB.next.next.next = ListNode(8)
# headB.next.next.next.next = ListNode(4)
# headB.next.next.next.next.next = ListNode(5)

# # 测试代码
# solution = Solution()
# intersection_node = solution.getIntersectionNode(headA, headB)

# if intersection_node:
#     print("Intersection node value:", intersection_node.val)
# else:
#     print("No intersection point.")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        listA = []
        listB = []
        while tempA is not None:
            listA.append(tempA)
            tempA = tempA.next
        while tempB is not None:
            listB.append(tempB)
            tempB = tempB.next
        while len(listA) > 1 and len(listB) > 1 and listA[-2] == listB[-2]:
            listA.pop()
            listB.pop()
        if listA[-1] == listB[-1]:
            return listB[-1]
        else:
            return None

# 创建链表A: 4 -> 1 -> 8 -> 4 -> 5
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

# 创建链表B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

# 测试代码
solution = Solution()
intersection_node = solution.getIntersectionNode(headA, headB)

if intersection_node:
    print("Intersection node value:", intersection_node.val)
else:
    print("No intersection point.")
