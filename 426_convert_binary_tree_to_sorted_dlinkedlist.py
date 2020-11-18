"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root

        curr = None
        stack = []
        node = root
        head = None
        tail = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
                continue

            node = stack.pop()

            if not curr:
                # no curr yet
                curr = node
                head = curr
            else:
                # has curr, link
                tail = node
                curr.right = node
                node.left = curr
                curr = node

            # continue iteration
            node = node.right

        # connect head and tail
        if tail:
            head.left = tail
            tail.right = head
        else:
            head.left = head
            head.right = head

        return head