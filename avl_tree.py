# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):
    """
    [MEMO] Remember the four rotate cases and how to figure out implementation:
    https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
    (basically draw out leftleft and rightright to figure out right rotate and left rotate)
    And remember how to rebalnce for the four cases
    Four function interfaces
    """

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # rebalance
        # Try out 4 cases
        # left left
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # left right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # right left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        # nothing needs to be changed
        return root

    def leftRotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        return y

    def rightRotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


# Driver program to test above function
myTree = AVL_Tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""

# Preorder Traversal
print("Preorder traversal of the", "constructed AVL tree is")
myTree.preOrder(root)
print()

# This code is contributed by Ajitesh Pathak
