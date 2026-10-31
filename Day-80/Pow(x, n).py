class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result

#Recursive Solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x