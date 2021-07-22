from typing import Dict, List
from collections import defaultdict


class Solution:
    def __init__(self, balances: Dict = None):
        self.balances = balances

    def rebalance(self):
        insufficient = {}
        redundant = {}
        for account, balance in self.balances.items():
            if balance < 100:
                insufficient[account] = balance
            elif balance > 100:
                redundant[account] = balance

        result = []
        for account_to in insufficient.keys():
            while insufficient[account_to] < 100:
                account_from = next(iter(redundant), None)
                if account_from is None:
                    raise RuntimeError("Insufficient funds for rebalance")

                amount = 100 - insufficient[account_to]
                if redundant[account_from] - 100 < amount:
                    amount = redundant[account_from] - 100

                redundant[account_from] -= amount
                insufficient[account_to] += amount
                output = f"From: {account_from}, To: {account_to}, Amount: {amount}"
                result.append(output)

                if redundant[account_from] == 100:
                    del redundant[account_from]

        return result


class Solution2:
    def __init__(self, balances: Dict = {}):
        self.balances = balances
        self.receivers = {}
        self.givers = {}

        for account, balance in self.balances.items():
            if balance < 100:
                self.receivers[account] = balance
            elif balance > 100:
                self.givers[account] = balance

    def minTransfers(self) -> int:
        return self.backtrack(0)

    def backtrack(self, count: int):
        if not self.receivers:
            return count

        receiver = next(iter(self.receivers), None)
        receiver_balance = self.receivers[receiver]
        amount = 100 - receiver_balance
        res = float("Inf")
        for giver in list(self.givers.keys()):
            giver_balance = self.givers[giver]
            giver_amount = giver_balance - 100
            if giver_amount >= amount:
                del self.receivers[receiver]
                self.givers[giver] -= amount
                res = min(res, self.backtrack(count + 1))
                self.givers[giver] += amount
                self.receivers[receiver] = receiver_balance
            elif giver_amount > 0:
                self.receivers[receiver] -= giver_amount
                del self.givers[giver]
                res = min(res, self.backtrack(count + 1))
                self.givers[giver] = giver_balance
                self.receivers[receiver] += giver_amount

        return res


def test_rebalance():
    balances = {"AU": 80, "US": 140, "MX": 110, "SG": 120, "FR": 70}
    solution = Solution(balances)
    result = solution.rebalance()
    print(result)


def test_backtrack():
    balances = {"a": 85, "b": 120, "c": 95}
    solution = Solution2(balances)
    result = solution.minTransfers()
    assert result == 2


if __name__ == "__main__":
    balances = {"a": 85, "b": 120, "c": 95}
    solution = Solution2(balances)
    result = solution.minTransfers()
    assert result == 2
