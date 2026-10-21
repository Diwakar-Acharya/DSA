class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n <= 1:
            return False

        total = 1

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i

                if i != n // i:
                    total += n // i

        return total == n