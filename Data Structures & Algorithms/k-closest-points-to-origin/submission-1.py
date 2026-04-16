class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min_heap = [{2.8: [0,2]}, ]
        # for _ in range(k):
        #    min_heap.pop()

        def distance(x1, y1, x2, y2):
            return math.sqrt(abs((x1 - x2)**2 + (y1 - y2)**2))
        
        x0 = 0
        y0 = 0
        min_heap = []
        for i, (x, y) in enumerate(points): # O(n log n)
            dist = distance(x0, y0, x, y)
            node = [dist, i, [x, y]]
            heapq.heappush(min_heap, node)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[-1])
        
        return res
