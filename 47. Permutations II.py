from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return(set(permutations(nums,len(nums))))
        
