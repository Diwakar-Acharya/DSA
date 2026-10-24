from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        # return "".join(sorted(s, key=lambda x: c[x], reverse=True))
        ks = sorted(c.keys(), key=lambda x: c[x], reverse=True)
        return "".join(k * c[k] for k in ks)