class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Solution with O(1) space
        [MEMO] XOR
        n ^ 0 = a
        n ^ n = 0
        n ^ m ^ n = (n ^ n) ^ m = 0 ^ m = m
        So just XOR everything together
        """
        result = 0
        for num in nums:
            result = result ^ num
        return result