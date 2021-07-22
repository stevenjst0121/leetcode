import time
from threading import Lock
from typing import Deque
from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.hisotry = defaultdict(deque)
        self.mutexs = {}
        self.WINDOW = 2  # 2 seconds
        self.MAX_COUNT = 5  # 5 calls in 2 seconds

    def request(self, name: str) -> bool:
        current_time = time.time()

        if name not in self.hisotry:
            self.hisotry[name].append(current_time)
            return True

        records = self.hisotry[name]
        self._purge_records(records, current_time - 2)
        if len(records) >= self.MAX_COUNT:
            return False

        records.append(current_time)
        return True

    def _purge_records(self, records: Deque, threshold: float) -> None:
        while records and records[0] < threshold:
            records.popleft()


def test_and_print(solution: Solution, name: str) -> bool:
    result = solution.request(name)
    if result:
        print(f"Successfully sent request with name={name}")
    else:
        print(f"Failed to send request with name={name}")


if __name__ == "__main__":
    solution = Solution()
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    test_and_print(solution, "Steven")
    print("Sleeping...")
    time.sleep(2)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
    test_and_print(solution, "Steven")
    time.sleep(0.5)
