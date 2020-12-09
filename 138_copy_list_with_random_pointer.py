# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.added = {}  # old node -> new node

    def copyRandomList(self, head: "Node") -> "Node":
        """Solution 1
        [MEMO] All python immutables are hashable, Objects which are instances of user-defined classes are hashable by default.
        https://docs.python.org/3/glossary.html#term-hashable
        """
        if not head:
            return None

        if head in self.added:
            return self.added[head]

        new = Node(head.val)
        self.added[head] = new
        new.next = self.copyRandomList(head.next)
        new.random = self.copyRandomList(head.random)
        return new

    def copyRandomList(self, head: "Node") -> "Node":
        """Draft 1
        Brute force to calculate index of a node, only 6%
        """
        if not head:
            return None

        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        nodes = [None] * length
        node = head
        index = 0
        while node:
            if nodes[index]:
                nodes[index].val = node.val
            else:
                nodes[index] = Node(node.val)

            if node.next:
                if not nodes[index + 1]:
                    nodes[index + 1] = Node(0)
                nodes[index].next = nodes[index + 1]

            if node.random:
                random_index = self.calculateIndex(node.random, length)
                if not nodes[random_index]:
                    nodes[random_index] = Node(0)
                nodes[index].random = nodes[random_index]

            node = node.next
            index += 1

        return nodes[0]

    def calculateIndex(self, node: "Node", length: int) -> int:
        count = 0
        while node:
            count += 1
            node = node.next
        return length - count
