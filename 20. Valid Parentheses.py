class Solution:
    def isValid(self, myStr: str) -> bool:
        stack = []
        OpenToClose = {")":"(","]":"[","}":"{"}
        
        for c in myStr:
            if c in OpenToClose:
                if stack and stack[-1] == OpenToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False 
