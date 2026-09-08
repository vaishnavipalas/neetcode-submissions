class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)

        max_heap = []

        heapq.heapify(max_heap)

        for cnt in counts.values():
            heapq.heappush(max_heap, -cnt)
        
        time = 0
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:

                rest = 1 + heapq.heappop(max_heap)

                if rest:
                    cooldown.append((rest, time + n))


            else:
                time = cooldown[0][1]

            if cooldown and cooldown[0][1] == time:
                    
                    heapq.heappush(max_heap, cooldown.popleft()[0])

        return time


