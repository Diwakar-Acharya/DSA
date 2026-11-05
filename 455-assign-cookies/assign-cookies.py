class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        i = 0  # Children pointer
        j = 0  # Cookies pointer

        while i < len(g) and j < len(s):

            if s[j] >= g[i]:
                i += 1

            j += 1

        return i