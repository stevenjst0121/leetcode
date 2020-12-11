# TODO Look at discussion, this one has no solution
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Draft 2
        Moving window solution, basically when include a new nums[j] and it causes the subarray[i:j+1] invalid
        Move i to the right most position so that subarray[i:j+1] is valid
        """
        max_size = 0
        curr_min, curr_max = nums[0], nums[0]
        i, j = 0, 0
        while j < len(nums):
            if nums[j] > curr_max:
                curr_max = nums[j]
                diff = nums[j] - curr_min
                if diff > limit:
                    # move i to right most valid position
                    curr_min = nums[j]
                    i = j - 1
                    while curr_max - nums[i] <= limit:
                        if nums[i] < curr_min:
                            curr_min = nums[i]
                        i -= 1
                    i += 1
            elif nums[j] < curr_min:
                curr_min = nums[j]
                diff = curr_max - nums[j]
                if diff > limit:
                    # move i to right most valid position
                    curr_max = nums[j]
                    i = j - 1
                    while nums[i] - curr_min <= limit:
                        if nums[i] > curr_max:
                            curr_max = nums[i]
                        i -= 1
                    i += 1

            # Got a valid subarray here
            size = j - i + 1
            if size > max_size:
                max_size = size
            j += 1
        return max_size

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Draft 1
        Brute force with break to exist loop when current array already exceeds limit
        """
        N = len(nums)
        max_size = 0
        for i in range(N):
            if i + max_size >= N:
                break
            curr_min = min(nums[i : i + max_size + 1])
            curr_max = max(nums[i : i + max_size + 1])
            for j in range(i + max_size, N):
                if nums[j] < curr_min:
                    curr_min = nums[j]
                elif nums[j] > curr_max:
                    curr_max = nums[j]
                diff = curr_max - curr_min
                if diff <= limit:
                    size = j - i + 1
                    if size > max_size:
                        max_size = size
                else:
                    break
        return max_size