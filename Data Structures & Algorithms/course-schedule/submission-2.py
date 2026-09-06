class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = dict()

        for i in range(numCourses):
            graph[i] = []


        for course, prereq in prerequisites:

            graph[course].append(prereq)

        curr_path = set()

        def dfs(course):

            if course in curr_path:
                return False

            if graph[course] == []:
                return True

            curr_path.add(course)

            for pre in graph[course]:

                if not dfs(pre):
                    return False

            curr_path.remove(course)
            graph[course] = []
            return True

        for i in range(numCourses):

            if not dfs(i):
                return False

        return True
        