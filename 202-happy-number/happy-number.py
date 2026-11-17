# class Solution:
#     def isHappy(self, n: int) -> bool:
        
#         seen = set()

#         while n != 1:
#             if n in seen:
#                 return False

#             seen.add(n)

#             total = 0

#             while n > 0:
#                 digit = n % 10
#                 total += digit * digit
#                 n //= 10

#             n = total

#         return True

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         used_num = {n: True}
#         while n != 1:
#             new_num = 0 
#             while n > 0:
#                 new_num += (n%10)**2
#                 n = n // 10
#             if used_num.get(new_num, False):
#                 return False
#             used_num[new_num] = True
#             n = new_num

#         return True

class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x:int) -> int:
            return sum(int(d) ** 2 for d in str(x))
        
        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1