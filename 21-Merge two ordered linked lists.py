#Merge two ordered linked lists
# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.next=None

# def newNode(key):
#     return Node(key)


# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.next = None

#     # return a new node
#     @staticmethod
#     def new_node(key):
#         return Node(key)

#     # merge two sorted linked lists
#     @staticmethod
#     def merge_two_lists(list1, list2):
#         dummy = None
#         cur = None

#         while list1 is not None and list2 is not None:
#             if list1.key < list2.key:
#                 if dummy is None:
#                     dummy = Node.new_node(list1.key)
#                     cur = dummy
#                 else:
#                     cur.next = Node.new_node(list1.key)
#                     cur = cur.next
#                 list1 = list1.next
#             else:
#                 if dummy is None:
#                     dummy = Node.new_node(list2.key)
#                     cur = dummy
#                 else:
#                     cur.next = Node.new_node(list2.key)
#                     cur = cur.next
#                 list2 = list2.next

#         while list1 is not None:
#             if dummy is None:
#                 dummy = Node.new_node(list1.key)
#                 cur = dummy
#             else:
#                 cur.next = Node.new_node(list1.key)
#                 cur = cur.next
#             list1 = list1.next

#         while list2 is not None:
#             if dummy is None:
#                 dummy = Node.new_node(list2.key)
#                 cur = dummy
#             else:
#                 cur.next = Node.new_node(list2.key)
#                 cur = cur.next
#             list2 = list2.next

#         return dummy
# """类的定义"""
# class LList:
#     def __init__(self):
#         self._head = None
    
#     def is_empty(self):
#         return self._head is None
    
#     def prepend(self,elem):
#         self._head = LNode(elem,self._head)

#     def pop(self):
#         if self._head is None:
#             raise LinkedListUnderflow("in pop")
#         e = self._head.elem
#         self._head=self._head.next
#         return e

# def filter(self,pred):
#     p = self._head
#     while p is not None:
#        if pred(p.elem):
#            yield p.elem
#         p = p.next

def pop_last(self):
    if self._head is None:
        raise LinkedinListUnderflow("in pop_last")
    p = self._head
    if p._next is None:
        e = p.elem
        self._head = None
        return e
    while p.next.next is not None：
        p = p.next
    e=p.next.elem
    p.next = None
    self._rear = p
    return e

mlist1 = LList1()
mlist1.prepend(99)
for i in range(11,20):
    mlist1.append(randint(1,20))

for x in mlist1.filter(lambda y:y%2==0):
    print(x)