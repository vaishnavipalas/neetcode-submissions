class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = {i:[] for i in range(numCourses)}
        pr_left = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            pr_left[course] += 1

        queue = deque()
        res = []

        for i in range(numCourses):

            if pr_left[i] == 0:
                queue.append(i)
                res.append(i)


        while queue:

            course = queue.popleft()

            for nxt in graph[course]:

                pr_left[nxt] -= 1

                if pr_left[nxt] == 0:
                    queue.append(nxt)
                    res.append(nxt)

        return res if len(res) == numCourses else []

        