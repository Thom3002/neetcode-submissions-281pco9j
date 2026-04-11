class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours_total = 0
            for p in piles:
                hours_total += (p + k - 1) // k
            return hours_total <= h
        
        left = 1
        right = max(piles)

        ans = h

        while left <= right:
            mid = (right + left) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans