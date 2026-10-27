class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                maximum = max(freq)
                minimum = min(f for f in freq if f > 0)

                total += maximum - minimum

        return total