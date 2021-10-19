class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        [MEMO] The way to use map to store last seen and update start
        """
        seen = {}
        max_length = 0
        start = 0
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)

            seen[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length
