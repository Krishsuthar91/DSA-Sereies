class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            count += 1
            n = n & (n - 1)

        return count


#Alternative solution using bit manipulation
class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count