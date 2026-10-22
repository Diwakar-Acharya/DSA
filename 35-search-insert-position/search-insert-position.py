class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        low, right = 0, len(nums)-1

        while low <= right:
            mid = low + (right-low) // 2 

            if nums[mid] > target: 
                right = mid - 1
            else:
                low = mid + 1
            
            if nums[mid] == target:
                return mid

        return low



        