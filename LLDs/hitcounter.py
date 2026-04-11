import collections

class ClickCounter:
    def __init__(self):
        self.clicks_queue = collections.deque()


    def recordClick(self, timestamp):
        self.clicks_queue.append(timestamp)


    def getRecentClicks(self, timestamp):
        # clean recent clicks
        while self.clicks_queue and self.clicks_queue[0] <= timestamp - 300:
            self.clicks_queue.popleft()

        return len(self.clicks_queue)


tracker = ClickCounter()

tracker.recordClick(1)
print("Clicks: ", tracker.clicks_queue)
tracker.recordClick(2)
print("Clicks: ", tracker.clicks_queue)
tracker.recordClick(3)
print("Clicks: ", tracker.clicks_queue)

print("recentClicks ", tracker.getRecentClicks(4))

tracker.recordClick(300)
print("Clicks: ", tracker.clicks_queue)

print("recentClicks ", tracker.getRecentClicks(300))

print("recentClicks ", tracker.getRecentClicks(301))
