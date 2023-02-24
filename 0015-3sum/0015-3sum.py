class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        nums.sort()
        
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sums = v + nums[l] + nums[r]

                if sums > 0:
                    r -= 1
                if sums < 0:
                    l += 1
                if sums == 0:
                    result.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result
            