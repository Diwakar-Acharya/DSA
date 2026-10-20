class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        position = 0
        position_odd = 1
        anws = [0] * len(nums)


        
        for i in range(len(nums)):

            if nums[i] < 0:
                
                if position_odd < len(nums):
                    anws[position_odd] = nums[i]
                    position_odd = position_odd + 2
            
            elif nums[i] >= 0:
                
                if position < len(nums):
                    anws[position] = nums[i]
                    position = position + 2

        return anws





        # for i in nums:
        #     if nums[i] >= 0 :
        #         nums[position] = nums[i]
        #         if position < len(nums):
        #             position = position + 2
            
        #     else:
        #         nums[position_odd] = nums[i]
        #         if position_odd < len(nums):
        #             position_odd = position_odd + 2
                



        