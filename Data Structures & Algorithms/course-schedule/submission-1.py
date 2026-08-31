class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        path = set()
        def dfs(course):

            if course in path:
                return False

            if graph[course] == []:
                return True

            path.add(course)

            for p in graph[course]:
                if not dfs(p):
                    return False
            path.remove(course)
            graph[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        