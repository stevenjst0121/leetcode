from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Solution 1
        [MEMO] Very similar idea to Draft 1, but smarter
        It is more efficient in:
            * Use stack in rcounter directly
                {1: [5, 7, 4], 2: [5, 7], 3: [5]}
            * Keep track of max freq so there is no need to find it in pop()
        """
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

    # def __init__(self):
    #     """Draft 1
    #     Use counter + reverse counter to find the element should be poped out
    #     """
    #     self.stack = []
    #     self.counter = {}
    #     self.rcounter = defaultdict(set)

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if val not in self.counter:
    #         self.counter[val] = 1
    #         self.rcounter[1].add(val)
    #     else:
    #         count = self.counter[val]
    #         self.rcounter[count].remove(val)
    #         self.counter[val] = count + 1
    #         self.rcounter[count + 1].add(val)
    #         if not self.rcounter[count]:
    #             del self.rcounter[count]
    #     assert True

    # def pop(self) -> int:
    #     max_count = max(self.rcounter.keys())
    #     vals = self.rcounter[max_count]
    #     to_pop = -1
    #     for i in range(len(self.stack) - 1, -1, -1):
    #         val = self.stack[i]
    #         if val in vals:
    #             to_pop = i
    #             break
    #     val = self.stack[to_pop]
    #     del self.stack[to_pop]
    #     count = self.counter[val]
    #     if count == 1:
    #         del self.counter[val]
    #         self.rcounter[count].remove(val)
    #         if not self.rcounter[count]:
    #             del self.rcounter[count]
    #     else:
    #         self.counter[val] -= 1
    #         self.rcounter[count].remove(val)
    #         self.rcounter[count - 1].add(val)
    #         if not self.rcounter[count]:
    #             del self.rcounter[count]

    #     return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
