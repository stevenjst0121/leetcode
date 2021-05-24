# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        """Draft 1
        DFS that returns double linked list (not circular) given a root
        """
        if not root:
            return None

        head, tail = self.dfs(root)
        tail.right = head
        head.left = tail
        return head

    def dfs(self, node: "Node"):
        assert node
        if not node.left and not node.right:
            return (node, node)

        curr_head = node
        curr_tail = node
        if node.left:
            head, tail = self.dfs(node.left)
            tail.right = node
            node.left = tail
            curr_head = head

        if node.right:
            head, tail = self.dfs(node.right)
            node.right = head
            head.left = node
            curr_tail = tail

        return (curr_head, curr_tail)


# class Solution:
#     def treeToDoublyList(self, root: "Node") -> "Node":
#         if not root:
#             return root

#         curr = None
#         stack = []
#         node = root
#         head = None
#         tail = None
#         while node or stack:
#             if node:
#                 stack.append(node)
#                 node = node.left
#                 continue

#             node = stack.pop()

#             if not curr:
#                 # no curr yet
#                 curr = node
#                 head = curr
#             else:
#                 # has curr, link
#                 tail = node
#                 curr.right = node
#                 node.left = curr
#                 curr = node

#             # continue iteration
#             node = node.right

#         # connect head and tail
#         if tail:
#             head.left = tail
#             tail.right = head
#         else:
#             head.left = head
#             head.right = head

#         return head