class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
    
        max_arr = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_arr
            max_arr = max(max_arr, temp)

        return arr

            