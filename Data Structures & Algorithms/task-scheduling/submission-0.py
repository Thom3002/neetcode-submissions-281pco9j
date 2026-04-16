class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = {}
        for task in tasks:
            if task in count:
                count[task] = count[task] + 1
            else:
                count[task] = 1

        max_heap = []
        for freq in count.values():
            max_heap.append(-freq)
        
        heapq.heapify(max_heap)

        queue = deque()
        t = 0
        while max_heap or queue:
            # queue = [[freq, idle_time]]
            t += 1
            if max_heap:
                freq = heapq.heappop(max_heap) + 1
                if freq < 0:
                    idle_time = t + n
                    queue.append([freq, idle_time])
            
            if queue:
                if queue[0][1] <= t:
                    heapq.heappush(max_heap, queue.popleft()[0])
            
        return t



