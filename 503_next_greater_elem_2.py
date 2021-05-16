from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """Draft 1
        Trick is to use iterations to track how many iterations are done
        """
        iterations = 1
        stack = []
        result = [-1] * len(nums)
        i = 0
        while iterations < 3 and i < len(nums):
            if stack:
                num = nums[i]
                while stack and stack[-1][1] < num:
                    item = stack.pop()
                    result[item[0]] = num

            stack.append((i, nums[i]))

            i += 1
            if i == len(nums):
                i = 0
                iterations += 1
        return result
