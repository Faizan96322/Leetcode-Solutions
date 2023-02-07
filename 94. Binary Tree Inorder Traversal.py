# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inordertraversal(root, res): 
            
            if root is not None:
                inordertraversal(root.left,res)
                lst.append(root.val)
                inordertraversal(root.right,res)
        lst = []  
        inordertraversal(root, lst)
        return lst
