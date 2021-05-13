from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Solution 1
        [MEMO] Using DP
        """
        N = len(prices)

        # Get left max profits
        min_price = None
        max_profit = 0
        max_profit_left = [0] * N
        for i in range(N):
            price = prices[i]
            if min_price is None:
                min_price = price
                continue

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            max_profit_left[i] = max_profit

            if price < min_price:
                min_price = price

        # Get right max profits
        max_price = None
        max_profit = 0
        max_profit_right = [0] * N
        for i in range(N - 1, -1, -1):
            price = prices[i]
            if max_price is None:
                max_price = price
                continue

            profit = max_price - price
            if profit > max_profit:
                max_profit = profit
            max_profit_right[i] = max_profit

            if price > max_price:
                max_price = price

        # Find max
        max_profit = 0
        for i in range(N):
            profit = max_profit_left[i] + max_profit_right[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit
