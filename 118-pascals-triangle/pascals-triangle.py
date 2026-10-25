class Solution:
    def generate(self, numIndex: int) -> list[list[int]]:
        result = []

        for i in range(numIndex):
            row = []
            ans = 1
            for r in range(i + 1):
                row.append(ans)
                ans = ans * (i - r) // (r + 1)
            
            result.append(row)

        
        
        
        return result
