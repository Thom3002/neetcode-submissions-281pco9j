class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)

        def get_heaviest_stone(max_heap):
            return -heapq.heappop(max_heap)

        while max_heap and len(max_heap) > 1:
            # pop two heaviest stones
            x = get_heaviest_stone(max_heap)
            y = get_heaviest_stone(max_heap)

            
            if y != x:
                x = x - y
                heapq.heappush(max_heap, -x)
            else:
                continue

        if max_heap:
            return -max_heap[0]
        return 0