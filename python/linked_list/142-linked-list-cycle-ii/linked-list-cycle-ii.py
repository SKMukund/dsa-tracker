# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        seen = {}

        while curr:
            if curr in seen:
                return curr
            else:
                seen[curr] = 1

            curr = curr.next
        return None
        