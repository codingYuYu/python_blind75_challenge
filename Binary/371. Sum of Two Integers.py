class Solution(object):
    def getSum(self, a, b):
        return sum([a,b])

class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF  # 32 bit mask
        maxInt = 2**31 - 1

        while b != 0:
            sum = (a ^ b) & mask # contain to 32 bits
            carry = (a & b) & mask # contain to 32 bits
            a = sum
            b = carry << 1

        return a if a <= maxInt else ~(a ^ mask)

    class Solution(object):
        def getSum(self, a, b):
            if a == 0 and b != 0:
                return b
            elif b == 0 and a != 0:
                return a

            return int(log(exp(a) * exp(b)))