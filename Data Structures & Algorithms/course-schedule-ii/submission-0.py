class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = {i:[] for i in range(numCourses)}
        prereqs_left = [0] * numCourses
        res = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereqs_left[course] += 1


        queue = deque()
        for i in range(numCourses):
            if prereqs_left[i] == 0:
                res.append(i)
                queue.append(i)

        while queue:

            curr_course = queue.popleft()

            for nxt in graph[curr_course]:
                prereqs_left[nxt] -= 1
                
                if prereqs_left[nxt] == 0:
                    queue.append(nxt)
                    res.append(nxt)

        return res if len(res) == numCourses else []

        