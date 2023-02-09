# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return 
        mid_num = len(nums)//2
        node = TreeNode(nums[mid_num])
        node.left = self.sortedArrayToBST(nums[:mid_num])
        node.right = self.sortedArrayToBST(nums[mid_num+1:])
        return node
            
