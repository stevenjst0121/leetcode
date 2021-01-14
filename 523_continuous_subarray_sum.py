from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Solution 3
        [MEMO+1] I was able to think of storing cumulative sum, but did not come up with an O(N) solution
        When think about solutions around using cum sum, think about how the diffs between two sums can help
        This is so fucking brilliant!!!
        """
        if not nums or len(nums) < 2:
            return False

        sums = {}  # sum % k till ith index
        sums[0] = -1
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            key = sum % k if k != 0 else sum
            if key in sums and sums[key] < i - 1:
                return True
            if key not in sums:
                # IMPORTANT: only care about the earliest index of this residule
                sums[key] = i
        return False

    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     """Draft 1
    #     Brute force, beats 10%
    #     """
    #     if not nums:
    #         return False

    #     start = 0
    #     curr = start + 1
    #     size = len(nums)
    #     while start < size - 1:
    #         sum = nums[start]
    #         while curr < size:
    #             sum += nums[curr]
    #             if k == 0:
    #                 if sum == 0:
    #                     return True
    #                 else:
    #                     break
    #             if sum == k or sum % k == 0:
    #                 return True
    #             curr += 1
    #         start += 1
    #         curr = start + 1
    #     return False
