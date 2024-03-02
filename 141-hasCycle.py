"""141
快慢指针：

输入为空，则一定不是环形链表；

定义慢指针p1和快指针p2，每次分别走一步和两步，如果快指针走到了链表结尾，说明不是链表不是环形；

如果存在环形结构，则快慢指针一定会相遇，返回True即可。

作者：玖月晴
链接：https://www.jianshu.com/p/6901e153c16a
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self,head):
        if not head:
          return False
        p1=p1=head
        while p1 and p1.next:
           p1=p1.next.next
           p2=p2.next
           if p1==p2:
              return True
        return False
          
