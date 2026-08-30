import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        result = []

        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(heap, (x*x+ y*y,[x,y]))

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        