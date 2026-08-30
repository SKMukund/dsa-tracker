import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)
            heapq.heappush(heap, -(largest - second_largest))
        
        return -heap[0]
