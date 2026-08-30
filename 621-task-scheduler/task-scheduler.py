import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = {}
        count = 0

        for task in tasks:
            if task in map:
                map[task] += 1
            else:
                map[task] = 1
        
        max_heap = [(-val, key) for key, val in map.items()]
        heapq.heapify(max_heap)

        while max_heap:
            temp = n + 1
            used = []
            while temp != 0 and max_heap:
                largest_val, largest_key = heapq.heappop(max_heap)
                count += 1
                largest_val += 1
                if largest_val != 0:
                    used.append((largest_val, largest_key))
                temp -= 1
            for item in used:
                heapq.heappush(max_heap, item)
            if max_heap:
                count += temp
        return count
