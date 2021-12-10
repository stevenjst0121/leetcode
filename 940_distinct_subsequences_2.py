class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # [MEMO]
        # Trick is to count empty sequence during DP and minus it in the end
        # Trick is to keep track of dp result prev of adding a certain letter, which represents duplicate when that letter appears again
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(2 * dp[-1])
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)
