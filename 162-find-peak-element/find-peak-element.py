class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        target = max(nums)
        return nums.index(target)
            

        
                
        