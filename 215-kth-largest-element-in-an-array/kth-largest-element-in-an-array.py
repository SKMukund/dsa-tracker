import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)
        
        for i in range(k):
            result = -heapq.heappop(heap)
        
        return result
        