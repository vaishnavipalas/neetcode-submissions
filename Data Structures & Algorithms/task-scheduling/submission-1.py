class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # greedy algo for the next task to always be the one with the highest freq
        # keep track of next highest frequent task with max_heap
        # if there is more of that task left, store it in a cooldown queue

        counts = Counter(tasks)

        max_heap = []

        for cnt in counts.values():
            max_heap.append(-cnt)

        heapq.heapify(max_heap)

        time = 0

        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                remaining = heapq.heappop(max_heap) + 1

                if remaining < 0:
                    cooldown.append((remaining, time + n))

            else:
                time = cooldown[0][1]

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time


