class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # greedy algo to determine which tasks to tackle first
        # use a pq for this

        # queue up when you can process the task again to add back to the pq

        # init time = 0 so we can see how long it will take
        # determine count of each task with a hashmap
        # for all the tasks, add them to the pq based on the frequency

        # init a queue to have it cooldown for the necessary amount of time

        # have a while loop while there are still tasks in the queue or pq to process

        # return the final time

        freqs = Counter(tasks)
        max_heap = []
        heapq.heapify(max_heap)
        time = 0

        for count in freqs.values():
            heapq.heappush(max_heap, -count)

        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                curr = heapq.heappop(max_heap) + 1

                if curr < 0:
                    cooldown.append((curr, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time

        