class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # sq = [x**2 for x in nums]
        # sq.sort()
        # return sq

        n = len(nums)
        for i in range(0,n,1):
            nums[i] = nums[i]*nums[i]
        
        nums.sort()
        
        return nums
        