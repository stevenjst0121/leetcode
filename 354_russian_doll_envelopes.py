class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        [MEMO] Standard way of finding LIS
        dp[i] represents LIS ending in i
        dp[i] = max(dp[j]) for each 0 <= j < i
        """
        envelopes.sort(key=lambda x: (x[0], -1 * x[1]))

        max_russian = 0
        dp = [0] * len(envelopes)
        for i in range(len(envelopes)):
            max_j = 0
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    max_j = max(max_j, dp[j])

            dp[i] = max_j + 1
            max_russian = max(max_russian, dp[i])
        return max_russian

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Solution
        [MEMO] Brilliant solution by sorting w in acsending and h in descending order
        [MEMO] The problem is really finding Longest Increasing Subsequence, but we can
        use the fact that all h should be non-increasing for the same w, use bisect_left
        """
        envelopes.sort(key=lambda x: (x[0], -1 * x[1]))

        stack = []
        for _, h in envelopes:
            idx = bisect_left(stack, h)
            if idx == len(stack):
                stack.append(h)
            else:
                stack[idx] = h
        return len(stack)

    def __init__(self):
        """Draft 1
        Backtrack works but exceeds time limit
        """
        self.max_russian = 0

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        self.backtrack(envelopes, [[0, 0]])
        return self.max_russian

    def backtrack(self, envelopes, dolls):
        if not envelopes:
            return

        for i, envelope in enumerate(envelopes):
            if envelope[0] > dolls[-1][0] and envelope[1] > dolls[-1][1]:
                dolls.append(envelope)
                self.max_russian = max(self.max_russian, len(dolls) - 1)
                self.backtrack(envelopes[i + 1 :], dolls)
                dolls.pop()