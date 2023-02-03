from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        return combinations(nums,k) 
