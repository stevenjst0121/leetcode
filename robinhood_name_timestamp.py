from collections import *


class Solution:
    def time_to_ts(self, t):
        return t // 100 * 60 + t % 100

    def ts_to_time(self, ts):
        return ts // 60 * 100 + ts % 60

    def findCheckinMoreThanThree(self, records):
        results = {}
        for name, timestamps in records.items():
            for i, ts in enumerate(timestamps):
                timestamps[i] = self.time_to_ts(ts)
            timestamps.sort()

            result = self.hasMoreThanThree(timestamps)
            for i, ts in enumerate(result):
                result[i] = self.ts_to_time(ts)
            if result:
                results[name] = result
        return results

    def hasMoreThanThree(self, timestamps):
        left, right = 0, 0
        queue = deque()
        while right < len(timestamps):
            if timestamps[right] - timestamps[left] <= 60:
                queue.append(timestamps[right])
                if len(queue) >= 3:
                    return list(queue)
                right += 1
            else:
                queue.popleft()
                left += 1
        return []


def test_case_1():
    solution = Solution()
    records = {"Steven": [855, 900, 915, 1025, 1129], "Tony": [856, 1000, 1135, 1155]}
    results = solution.findCheckinMoreThanThree(records)
    assert results == {"Steven": [855, 900, 915]}