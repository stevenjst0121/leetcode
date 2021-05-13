class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        [MEMO] Make draft 1 work by looping from the end
        """
        N = len(s)
        is_palindrome = [[0] * N for _ in range(N)]

        max_palindrome = s[0]
        max_len = 1
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if i == j:
                    is_palindrome[i][j] = 1
                elif j == i + 1:
                    if s[i] == s[j]:
                        is_palindrome[i][j] = 1
                else:
                    if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = 1

                curr_len = j - i + 1
                if is_palindrome[i][j] and curr_len > max_len:
                    max_palindrome = s[i : j + 1]
                    max_len = curr_len

        return max_palindrome

    def longestPalindrome(self, s: str) -> str:
        """Draft 1
        Bottom-up DP, works but exceeds time limit
        """
        N = len(s)
        is_palindrome = [[0] * N for _ in range(N)]

        max_palindrome = None
        max_len = 0
        curr_len = 1
        while curr_len <= N:
            for i in range(0, N - curr_len + 1):
                for j in range(i + curr_len - 1, N):
                    if i == j:
                        is_palindrome[i][j] = 1
                    elif j == i + 1:
                        if s[i] == s[j]:
                            is_palindrome[i][j] = 1
                    else:
                        if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                            is_palindrome[i][j] = 1

                    if is_palindrome[i][j] and curr_len > max_len:
                        max_palindrome = s[i : j + 1]
                        max_len = curr_len
            curr_len += 1

        print(is_palindrome)
        return max_palindrome
