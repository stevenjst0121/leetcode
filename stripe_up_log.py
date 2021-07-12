from typing import List


class Solution:
    def compute_penalty(self, log: str, remove_at: int) -> int:
        up_down = log.split(" ")
        penalty = 0
        for i, status in enumerate(up_down):
            if i < remove_at and status == "1" or i >= remove_at and status == "0":
                penalty += 1

        return penalty

    def find_best_removal(self, log: str) -> int:
        N = len(log.split(" "))
        min_penalty = float("Inf")
        result = -1
        for i in range(N + 1):
            penalty = self.compute_penalty(log, i)
            if penalty < min_penalty:
                min_penalty = penalty
                result = i
        return result

    def get_best_removal_times(self, log: str) -> List[int]:
        log_lines = log.splitlines()
        result = []
        stack = []
        for line in log_lines:
            details = line.split(" ")
            for content in details:
                if content == "BEGIN":
                    stack = [content]
                elif content == "END":
                    if len(stack) > 1:
                        result.append(self.find_best_removal(" ".join(stack[1:])))
                    stack = []
                elif content in ("0", "1"):
                    if stack:
                        stack.append(content)
        return result


def test_case_1():
    solution = Solution()
    result = solution.compute_penalty("0 0 1 0", 0)
    assert result == 3

    result = solution.compute_penalty("0 0 1 0", 4)
    assert result == 1

    result = solution.compute_penalty("", 0)
    assert result == 0


def test_case_2():
    solution = Solution()
    result = solution.find_best_removal("0 0 1 1")
    assert result == 2


def test_case_3():
    solution = Solution()
    result = solution.get_best_removal_times("BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN")
    assert result == [2]
