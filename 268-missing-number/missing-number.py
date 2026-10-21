class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            if i not in nums:
                return i
            elif n not in nums:
                return n

        