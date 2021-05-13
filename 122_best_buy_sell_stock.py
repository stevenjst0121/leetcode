from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Solution 3
        Super simple one pass, because incremental profit equals to total profit
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        """Draft 1
        Beats 99%, be careful to use min_price is (not) None becaue price can be 0
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = None
        profit = 0

        N = len(prices)
        for i in range(N - 1):
            price = prices[i]
            if min_price is None:
                min_price = price
                continue

            next_price = prices[i + 1]
            if next_price < price:
                if price > min_price:
                    # sell at current price
                    profit += price - min_price
                    min_price = None
                else:
                    # update min price
                    min_price = price
            else:
                # hold it, it's still going up
                if price < min_price:
                    min_price = price

        if min_price is not None and prices[-1] > min_price:
            profit += prices[-1] - min_price

        return profit