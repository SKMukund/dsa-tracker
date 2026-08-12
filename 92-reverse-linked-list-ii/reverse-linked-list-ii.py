# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        i = 1

        dummy = ListNode(0)
        dummy.next = head
        left_node = dummy

        reverse_tail = None

        while curr:
            if i < left:
                left_node = left_node.next

            if i >= left and i <= right:
                if i == left:
                    reverse_tail = curr

                next_curr = curr.next
                curr.next = prev

                prev = curr
                curr = next_curr

            elif i > right:
                break

            else:
                curr = curr.next
            i += 1
        left_node.next = prev
        reverse_tail.next = curr

        return dummy.next

        