# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        dummyHead = TreeNode()
        dummyHead.next = head
        slow = dummyHead
        fast = dummyHead
        while fast.next and fast.next.next:
            """
            Tip: Draw the situations with even and odd number in list
            Make sure to find the middle one as root for odd number list,
            so that the BST will be balanced
            """
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        root = ListNode(right.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right.next)
        return root
