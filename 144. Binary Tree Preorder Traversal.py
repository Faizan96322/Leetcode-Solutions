# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preordertraversal(root, res): 
            
            if root is not None:
                lst.append(root.val)
                preordertraversal(root.left,res)
                
                preordertraversal(root.right,res)
        lst = []  
        preordertraversal(root, lst)
        return lst
