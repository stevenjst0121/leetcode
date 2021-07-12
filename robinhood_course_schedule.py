from typing import List, Dict
from collections import defaultdict, deque
import math


class Solution:
    def getMiddleCourse(self, prerequisites: List[List[str]]) -> str:
        in_degrees = {}
        graph = defaultdict(list)

        for course_a, course_b in prerequisites:
            if course_a not in in_degrees:
                in_degrees[course_a] = 0
            if course_b not in in_degrees:
                in_degrees[course_b] = 0

            graph[course_a].append(course_b)
            in_degrees[course_b] += 1

        result = []
        queue = deque(course for course, degree in in_degrees.items() if degree == 0)
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        mid = (len(result) - 1) // 2
        return result[mid]

    def getAllMiddleCourses(self, prerequisites: List[List[str]]) -> List[str]:
        in_degrees = {}
        graph = defaultdict(list)

        for course_a, course_b in prerequisites:
            if course_a not in in_degrees:
                in_degrees[course_a] = 0
            if course_b not in in_degrees:
                in_degrees[course_b] = 0

            graph[course_a].append(course_b)
            in_degrees[course_b] += 1

        results = []
        for course, degree in in_degrees.items():
            if degree > 0:
                continue

            paths = self.getAllPaths(course, graph)
            results.extend(paths)

        mids = set()
        for result in results:
            mid = math.ceil(len(result) / 2) - 1
            mids.add(result[mid])
        return list(mids)

    def getAllPaths(self, course: str, graph: Dict) -> List[List[str]]:
        if not graph[course]:
            return [[course]]

        result = []
        for neighbor in graph[course]:
            paths = self.getAllPaths(neighbor, graph)
            for path in paths:
                result.append([course] + path)
        return result


def test_case_1():
    solution = Solution()
    result = solution.getMiddleCourse(
        [["Data Structures", "Algorithms"], ["COBOL", "Networking"], ["Algorithms", "COBOL"]]
    )
    assert result == "Algorithms"


def test_case_2():
    solution = Solution()
    result = solution.getAllMiddleCourses(
        [
            ["Logic", "COBOL"],
            ["Data Structures", "Algorithms"],
            ["Creative Writing", "Data Structures"],
            ["Algorithms", "COBOL"],
            ["Intro to Computer Science", "Data Structures"],
            ["Logic", "Compilers"],
            ["Data Structures", "Logic"],
            ["Graphics", "Networking"],
            ["Networking", "Algorithms"],
            ["Creative Writing", "System Administration"],
            ["Databases", "System Administration"],
            ["Creative Writing", "Databases"],
            ["Intro to Computer Science", "Graphics"],
        ]
    )
    assert set(result) == set(["Data Structures", "Databases", "Creative Writing", "Networking"])
