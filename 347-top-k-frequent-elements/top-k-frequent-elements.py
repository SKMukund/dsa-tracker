import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        result = []

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        max_heap = [(-val, key) for key, val in map.items()]  
        heapq.heapify(max_heap)
        
        for i in range(k):
            largest_val, largest_key = heapq.heappop(max_heap)
            result.append(largest_key)
        
        return result

        