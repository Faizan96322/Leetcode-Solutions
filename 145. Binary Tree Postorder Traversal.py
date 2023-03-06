# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postordertraversal(root, res): 
            
            if root is not None:
                
                postordertraversal(root.left,res)
                
                postordertraversal(root.right,res)
                
                lst.append(root.val)
        lst = []  
        postordertraversal(root, lst)
        return lst
