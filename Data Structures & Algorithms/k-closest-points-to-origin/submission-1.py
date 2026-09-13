class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = (point[0]**2) + (point[1]**2)
            heap.append((dist, point[0], point[1]))

        heapq.heapify(heap)
        res = []

        for _ in range(k):
            _, p1, p2 = heapq.heappop(heap)
            res.append([p1,p2])
        
        return res

        