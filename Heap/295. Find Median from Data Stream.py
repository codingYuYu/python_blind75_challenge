class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, (-1)*num)
        if self.large and ((-1)*self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)*(-1)
            heapq.heappush(self.large,val)
        if len(self.small) == len(self.large)+2:
            val = heapq.heappop(self.small)*(-1)
            heapq.heappush(self.large,val)
        if len(self.small)+2 == len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val*(-1))

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (self.small[0]*(-1)+self.large[0])/2
        elif len(self.small) > len(self.large):
            return self.small[0]*(-1)
        else:
            return self.large[0]