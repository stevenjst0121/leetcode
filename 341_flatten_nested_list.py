# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedIntege]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """Solution
        [MEMO] Trick here is to define a makeStackTopAnInteger function
        Make use of reversed() built-in
        """
        self._stack = list(reversed(nestedList))

    def next(self) -> int:
        self.makeStackTopAnInteger()
        return self._stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.makeStackTopAnInteger()
        return self._stack

    def makeStackTopAnInteger(self):
        while self._stack and not self._stack[-1].isInteger():
            self._stack.extend(reversed(self._stack.pop().getList()))

    # def __init__(self, nestedList: [NestedInteger]):
    #     """Draft 1
    #     Use stack to flatten the list into new container, see solution to
    #     directly loop through iterator
    #     """
    #     self._stack = deque(nestedList)
    #     self._flat = []

    #     while self._stack:
    #         next_item = self._stack.popleft()
    #         if next_item.isInteger():
    #             self._flat.append(next_item.getInteger())
    #             continue

    #         next_list = next_item.getList()
    #         for i in range(len(next_list) - 1, -1, -1):
    #             self._stack.appendleft(next_list[i])

    #     self._curr = 0

    # def next(self) -> int:
    #     if not self.hasNext():
    #         raise RuntimeError()

    #     result = self._flat[self._curr]
    #     self._curr += 1
    #     return result

    # def hasNext(self) -> bool:
    #     return self._curr < len(self._flat)