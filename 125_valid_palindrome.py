class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Two Pointers
        [MEMO] String APIs: isalnum(), lower(), upper()
        """
        if not s:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True