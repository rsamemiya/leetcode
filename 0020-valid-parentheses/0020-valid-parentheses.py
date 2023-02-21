class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #if s.length is not <= 2 or s.length % 2 != 0then return None because you need to at least have an open and close bracket of itself, so an even number as well. 

        
        
        stack = []
        
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False
                