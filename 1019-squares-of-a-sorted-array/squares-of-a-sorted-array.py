class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sq = [x**2 for x in nums]
        sq.sort()
        return sq
        