# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = head
        count = 0

        while dummy:
            count += 1
            dummy = dummy.next
        
        mid = (count ) // 2

        curr = head
        for i in range(mid):
            curr = curr.next
        
        return curr

        