class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Two pointer
        O(N)
        """
        return self.helper(s, True)

    def helper(self, s: str, can_delete: bool) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if not can_delete:
                    return False
                else:
                    res_i = self.helper(s[i + 1 : j + 1], False)
                    res_j = self.helper(s[i:j], False)
                    return res_i or res_j

            i += 1
            j -= 1
        return True