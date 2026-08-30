import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        result = ""

        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        
        max_heap = [(-val, key) for key, val in map.items()]
        heapq.heapify(max_heap)

        prev_char = ""
        prev_count = 0
        while max_heap:
            largest_val, largest_key = heapq.heappop(max_heap)
            result += largest_key
            largest_val += 1

            if prev_char != "" and prev_count != 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            prev_char = largest_key
            prev_count = largest_val

        return result if len(result) == len(s) else ""

        