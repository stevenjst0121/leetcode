"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.added = {}

    def cloneGraph(self, node: "Node") -> "Node":
        """
        [MEMO] Fisrt draft, Use stack + visited to BFS traverse through a graph
        """
        if not node:
            return None

        if node.val in self.added:
            return self.added[node.val]

        new = Node(node.val)
        self.added[node.val] = new

        for neighbor in node.neighbors:
            new.neighbors.append(self.cloneGraph(neighbor))

        return new

    # def cloneGraph(self, node: "Node") -> "Node":
    #     """
    #     [MEMO] Fisrt draft, Use stack + visited to BFS traverse through a graph
    #     """
    #     # Traverse the graph and create dict
    #     d = {}  # val -> [val]
    #     stack = [node]
    #     while stack:
    #         curr = stack.pop()
    #         if curr.val not in d:
    #             d[curr.val] = [neighbor.val for neighbor in curr.neighbors]
    #             stack.extend(curr.neighbors)

    #     # Reconstruct graph
    #     added = {}
    #     new_node = Node(1)
    #     added[1] = new_node  # val -> node
    #     stack = [new_node]
    #     while stack:
    #         curr = stack.pop()
    #         vals = d[curr.val]
    #         for val in vals:
    #             if val not in added:
    #                 adding = Node(val)
    #                 curr.neighbors.append(adding)
    #                 added[val] = adding
    #                 stack.append(adding)
    #             else:
    #                 curr.neighbors.append(added[val])
    #     return new_node
