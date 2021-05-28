class MinStack:
    def __init__(self):
        """Solution 1
        [MEMO]
        Own idea was to use double-linked list to store vals in sorted order
        but that would take more time complexity and space.

        Store current min along with the val in stack
        Solution 2 using two stacks is also great, saves more space
        """
        self._stack = []

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append((val, val))
            return

        curr_min = self._stack[-1][1]
        self._stack.append((val, min(val, curr_min)))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]

    def __init__(self):
        """Solution 2"""
        self.stack = []
        self.min_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_tracker or val <= self.min_tracker[-1]:
            self.min_tracker.append(val)

    def pop(self) -> None:
        if not self.stack:
            return

        val = self.stack.pop()
        if val == self.min_tracker[-1]:
            self.min_tracker.pop()

    def top(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_tracker:
            return -1

        return self.min_tracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
