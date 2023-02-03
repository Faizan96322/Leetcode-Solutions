from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        for i in range(0,len(nums)+1):
            for j in combinations(nums,i):
                lst.append(j) 
        return lst
