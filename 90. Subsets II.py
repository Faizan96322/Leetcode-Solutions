from itertools import combinations
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=set()
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                ans.add(j)
        return ans 
