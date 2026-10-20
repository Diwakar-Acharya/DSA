class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        # for i in range(len(arr)):
        #     if i == (len(arr) - 1):
        #         arr[i] = -1
        #         break

        #     max_arr = 0

        #     for j in range(i+1, len(arr)):
        #         max_arr = max(max_arr, arr[j])
        #     arr[i] = max_arr
        
        # return arr

    
        max_arr = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_arr
            max_arr = max(max_arr, temp)

        return arr

            