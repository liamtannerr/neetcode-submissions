import math

def dist(point:List[int]) -> int:
    return (point[0]**2)+(point[1]**2)

class PointsHeap:

    def __init__(self, points: List[List[int]]):

        self.points = []
        self.distances = {}

        for point in points:
            self.add(point)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        cur = len(self.points) - 1
        parent = (cur - 1) // 2
        cur_dist = dist(point)
        self.distances[cur] = cur_dist
        while parent >= 0 and self.distances[parent] > cur_dist:
            self.swap(parent, cur)
            cur = parent
            parent = (cur - 1) // 2

    def rm (self) -> List[int]:

        if len(self.points) == 1:
            return self.points.pop()

        root = self.points[0]
        self.points[0] = self.points.pop()
        size = len(self.points)
        self.distances[0] = self.distances[size]
        del self.distances[size]

        cur = 0

        while True:
            left = (2 * cur) + 1
            right = (2 * cur) + 2
            smallest = cur
            
            if left < size and self.distances[left] < self.distances[smallest]:
                smallest = left
                
            if right < size and self.distances[right] < self.distances[smallest]:
                smallest = right
                
            if smallest == cur:
                break
                
            self.swap(cur, smallest)
            cur = smallest

        return root

    def swap(self, parent:int, child:int) -> None:

        temp = self.points[parent]
        self.points[parent] = self.points[child]
        self.points[child] = temp
        temp_dist = self.distances[parent]
        self.distances[parent] = self.distances[child]
        self.distances[child] = temp_dist


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = PointsHeap(points)
        res = []
        for _ in range(k):
            res.append(heap.rm())
        
        return res

        