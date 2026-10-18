class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp_list = []

        i = 0

        while i < len(nums):
            temp_list.append(nums[i])
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            i += 1

        nums[:len(temp_list)] = temp_list
            
        return len(temp_list)





                        