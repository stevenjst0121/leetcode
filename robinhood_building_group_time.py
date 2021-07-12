from typing import List


class Solution:
    def maxFreq(self, timestamps: List[int]) -> int:
        left, right = 0, 0
        max_freq = 0
        freq = 0
        while right < len(timestamps):
            if timestamps[right] - timestamps[left] <= 60:
                # expand
                freq += 1
                max_freq = max(max_freq, freq)
                right += 1
            else:
                # contract
                freq -= 1
                left += 1
        return max_freq


def test_case_1():
    solution = Solution()
    result = solution.maxFreq([1, 6, 61, 71, 81, 100, 120, 300])
    assert result == 5
