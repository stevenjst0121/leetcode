class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False

        self.map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False

        if self.data[-1] == val:
            self.data.pop()
            del self.map[val]
        else:
            index = self.map[val]
            last = self.data[-1]
            self.data[index], self.data[-1] = self.data[-1], self.data[index]
            self.data.pop()
            del self.map[val]
            self.map[last] = index
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = random.randint(0, len(self.data) - 1)
        return self.data[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()