class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}
        heap = []
        cooldown = collections.deque()

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        for task in freq:
            heapq.heappush(heap, -freq[task])

        del freq
        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    cooldown.append([freq, n + time])
            
            if cooldown and cooldown[0][1] == time:
                cooled_freq, _ = cooldown.popleft()
                heapq.heappush(heap, cooled_freq)

        return time