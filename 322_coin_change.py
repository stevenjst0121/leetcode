from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Solution 3
        [OPTIONAL MEMO] DP bottom up
        """
        counts = [float("inf")] * (amount + 1)
        counts[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                counts[x] = min(counts[x], counts[x - coin] + 1)
        print(counts)
        return counts[amount] if counts[amount] != float("inf") else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """Draft 1
        Recursion + memoization
        Time limit exceeded for some reason but I can run test just fine
        [429,171,485,26,381,31,290]
        8440
        """
        coins.sort()
        self.memo = {}  # (coins, amount) -> res
        return self.helper(coins, amount)

    def helper(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        if (tuple(coins), amount) in self.memo:
            return self.memo[(tuple(coins), amount)]

        biggest = coins[-1]
        num = amount // biggest
        res = []
        while num >= 0:
            sum = biggest * num
            if sum == amount:
                self.memo[(tuple(coins), amount)] = num
                return num

            ans = self.helper(coins[:-1], amount - sum)
            if ans > 0:
                self.memo[(tuple(coins), amount)] = num + ans
                res.append(num + ans)

            num -= 1

        if not res:
            self.memo[(tuple(coins), amount)] = -1
            return -1
        else:
            self.memo[(tuple(coins), amount)] = min(res)
            return min(res)