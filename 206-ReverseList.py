class ListNode:
    def _init_(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def ReverseList(self,pHead):
        if not pHead or not pHead.next:
            return pHead
        last=None
        while pHead:
            tmp=pHead.next
            pHead.next=last
            
            last=pHead
            pHead=tmp
        return last
    

    # def reverse_list(head):
    #         if head is None:
    #             return head
    #         cur = head
    #         pre = None
          
    #         while cur:
    #             tmp =cur.next
    #             cur.next= pre
    #             pre = cur
    #             cur = tmp         
    #         return pre
