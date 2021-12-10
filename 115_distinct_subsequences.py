class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # [MEMO] Brilliant DP solution
        # dp[i][j] represents num of distinct subsequences in s[i:] for t[j:]
        # super smart for handling dp[M][N] initial cases (see solution for explanation)

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    def numDistinct(self, s: str, t: str) -> int:
        # [MEMO]
        # It happens that in previous dp of 2D array, we only really need the next row
        # We can instead use an 1D array and update the values in-place

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [0 for j in range(N)]

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):

            # At each step we start with the last value in
            # the row which is always 1. Notice how we are
            # starting the loop from N - 1 instead of N like
            # in the previous solution.
            prev = 1

            for j in range(N - 1, -1, -1):

                # Record the current value in this cell so that
                # we can use it to calculate the value of dp[j - 1]
                old_dpj = dp[j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[j] += prev

                # Update the prev variable
                prev = old_dpj

        return dp[0]