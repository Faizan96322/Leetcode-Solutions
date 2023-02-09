# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, node):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not node:
            return None
        if not node.next:
            return TreeNode(node.val)
        slow = fast = node
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(node)
        root.right = self.sortedListToBST(slow.next)

        return root
