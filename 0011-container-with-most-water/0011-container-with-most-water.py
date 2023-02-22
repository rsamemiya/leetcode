class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            area = (r-l) * min(height[r], height[l])
            res = max(res, area)
            
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else :
                l += 1
        return res