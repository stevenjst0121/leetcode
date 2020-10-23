class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                # Remove start or remove end
                return self.isPalindrome(s, start + 1, end) or self.isPalindrome(s, start, end - 1)

        return True

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return True

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True