class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = list(set(nums)) # remove duplicates
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
