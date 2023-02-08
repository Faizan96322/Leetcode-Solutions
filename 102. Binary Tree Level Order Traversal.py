# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if not root:
        #     return []
        # q=[]
        # q.append(root)
        # while q!=0:
        #     root = q.pop(0)
        #     print(root)
        #     if root.left is not None:
        #         q.append(root.left)
        #     if root.right is not None:
        #         q.append(root.right)
        
        
        if not root:
            return []
        q=[]
        q.append(root)
        res=[]
        while(q):
            size=len(q)
            l=[]
            for _ in range(size):
                temp=q.pop(0)
                l.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(l)
        return res
