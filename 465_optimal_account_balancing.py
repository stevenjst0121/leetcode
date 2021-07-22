class Solution:
    def __init__(self):
        self.balances = defaultdict(int)
        self.receivers = []
        self.givers = []

    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        [MEMO] Backtrack solution using balances, receiver + giver
        Works but exceeds time limit
        """
        for transaction in transactions:
            self.balances[transaction[0]] -= transaction[2]
            self.balances[transaction[1]] += transaction[2]

        for i, balance in self.balances.items():
            if balance > 0:
                self.receivers.append(i)
            else:
                self.givers.append(i)

        return self.traverse(0, 0)

    def traverse(self, receiver_index: int, count: int):
        if receiver_index >= len(self.receivers):
            return count

        receiver = self.receivers[receiver_index]
        amount = self.balances[receiver]
        res = float("Inf")
        for giver_index in range(len(self.givers)):
            giver = self.givers[giver_index]
            giver_amount = -1 * self.balances[giver]
            if giver_amount >= amount:
                self.balances[giver] += amount
                self.balances[receiver] -= amount
                res = min(res, self.traverse(receiver_index + 1, count + 1))
                self.balances[receiver] += amount
                self.balances[giver] -= amount
            elif giver_amount > 0:
                self.balances[giver] += giver_amount
                self.balances[receiver] -= giver_amount
                res = min(res, self.traverse(receiver_index, count + 1))
                self.balances[receiver] += giver_amount
                self.balances[giver] -= giver_amount

        return res

    def __init__(self):
        self.balances = defaultdict(int)
        self.debts = []

    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        [MEMO] Brilliant backtrack solution with debts only
        """
        for transaction in transactions:
            self.balances[transaction[0]] -= transaction[2]
            self.balances[transaction[1]] += transaction[2]

        for i, balance in self.balances.items():
            if balance != 0:
                self.debts.append(balance)

        return self.traverse(0)

    def traverse(self, i: int):
        while i < len(self.debts) and self.debts[i] == 0:
            i += 1

        res = float("Inf")
        for j in range(i + 1, len(self.debts)):
            if self.debts[i] > 0 and self.debts[j] < 0 or self.debts[i] < 0 and self.debts[j] > 0:
                self.debts[j] += self.debts[i]
                res = min(res, 1 + self.traverse(i + 1))
                self.debts[j] -= self.debts[i]
        return res if res < float("Inf") else 0
