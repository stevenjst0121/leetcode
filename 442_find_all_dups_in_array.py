class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """Solution
        [MEMO] Original idea was similar, but was using -1 for seen values
        this would cause duplicates to be added to result
        Simply change the index num to its negative value, and use abs() for checking
        """
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] *= -1

        return result