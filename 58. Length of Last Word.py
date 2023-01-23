class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lst = s.split()
        s = lst[-1]
        return len(s)
