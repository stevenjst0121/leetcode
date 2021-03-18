# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    """Solution
    [MEMO] Improved version of draft 2
    Use stack and pop(0) to avoid copy
    And change deserialize interface to take data list only and return root
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        output = []
        self.serialize_dfs(root, output)
        return ",".join([str(item) for item in output])

    def serialize_dfs(self, node, output):
        if not node:
            output.append(node)
            return

        output.append(node.val)
        self.serialize_dfs(node.left, output)
        self.serialize_dfs(node.right, output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = self.deserialize_dfs(data)
        return root

    def deserialize_dfs(self, data):
        if not data:
            return None

        if data[0] == "None":
            data.pop(0)
            return None

        root = TreeNode(int(data[0]))
        data.pop(0)
        root.left = self.deserialize_dfs(data)
        root.right = self.deserialize_dfs(data)

        return root


class Codec:
    """Second Draft
    [MEMO] Use DFS pre-order traversal, it's better because its sequence suits more
    to the root - node relationship, but still only beats 5%
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        output = []
        self.serialize_dfs(root, output)
        return ",".join([str(item) for item in output])

    def serialize_dfs(self, node, output):
        if not node:
            output.append(node)
            return

        output.append(node.val)
        self.serialize_dfs(node.left, output)
        self.serialize_dfs(node.right, output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        self.deserialize_dfs(root, data[1:])
        return root

    def deserialize_dfs(self, root, data):
        if not root or not data:
            return data

        left = TreeNode(int(data[0])) if data[0] != "None" else None
        root.left = left
        data = self.deserialize_dfs(root.left, data[1:])

        right = TreeNode(int(data[0])) if data[0] != "None" else None
        root.right = right
        data = self.deserialize_dfs(root.right, data[1:])

        return data


class Codec:
    """1st Draft
    Same serialization logic as leetcode
    It works, but exceeds time limit
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        output = []
        queue = deque([root])
        while queue:
            if not any(queue):
                # All items are None
                break

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    output.append("null")
                    queue.append(None)
                    queue.append(None)
                else:
                    output.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
        return ",".join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        pre_nodes = deque([root])
        level = 1
        low = 1
        while low < len(data):
            high = low + 2 ** level
            while low < high:
                node = pre_nodes.popleft()
                left = TreeNode(int(data[low])) if data[low] != "null" else None
                right = TreeNode(int(data[low + 1])) if data[low + 1] != "null" else None
                if left:
                    node.left = left
                if right:
                    node.right = right
                pre_nodes.append(left)
                pre_nodes.append(right)
                low += 2
            level += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))