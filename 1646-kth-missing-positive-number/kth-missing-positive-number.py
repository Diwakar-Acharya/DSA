class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr2 = list(range(1, arr[-1] + k + 1))

        for num in arr:
            arr2.remove(num)

        return arr2[k - 1]