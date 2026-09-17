class MedianFinder:

    def __init__(self):

        self.min_heap = []
        self.min_size = 0
        self.max_heap = []
        self.max_size = 0

    def addNum(self, num: int) -> None:
          
        if not self.min_heap or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            self.min_size += 1       
        else:
            heapq.heappush(self.max_heap, -num)
            self.max_size += 1

        if (self.min_size - self.max_size) > 1:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)
            self.min_size -= 1
            self.max_size += 1
        elif (self.max_size - self.min_size) > 1:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)
            self.min_size += 1
            self.max_size -= 1

    def findMedian(self) -> float:

        if (self.min_size + self.max_size) % 2 == 0:
            return float((-self.max_heap[0] + self.min_heap[0]) / 2)
        elif (self.min_size > self.max_size):
            return float(self.min_heap[0])
        else:
            return float(-self.max_heap[0])
              