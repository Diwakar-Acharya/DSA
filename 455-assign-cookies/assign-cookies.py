# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:

#         g.sort()
#         s.sort()

#         i = 0  # Children pointer
#         j = 0  # Cookies pointer

#         while i < len(g) and j < len(s):

#             if s[j] >= g[i]:
#                 i += 1

#             j += 1

#         return i

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if len(s) == 0:
            return 0
        
        # O(N log N)
        g.sort()
        s.sort()
        
        cookie_i, n_cookies = 0, len(s)
        child_i, n_children = 0, len(g)
        
        result = 0
        while child_i < n_children and cookie_i < n_cookies:
            
            if g[child_i] > s[cookie_i]:
                cookie_i += 1  # try next cookie
                continue
            
            result += 1
            cookie_i += 1
            child_i += 1

        return result
        # g = [1,2,3], s = [1,1]
        # g = [1,2], s = [1,2,3]
        # g = [10,9,8,7], s = [5,6,7,8]