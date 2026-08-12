# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = head
        count = 0
        
        while dummy:
            dummy = dummy.next
            count += 1

        prev = ListNode(0)
        prev.next = head
        curr = prev
        i = -1
        while curr and curr.next:
            if i == (count - n - 1):
                curr.next = curr.next.next
            else:
                curr = curr.next
            i += 1
        
        return prev.next
            
