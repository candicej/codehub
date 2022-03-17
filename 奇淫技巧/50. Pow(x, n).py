# 快速幂算法
# 不太理解，
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            # 如果当前位
            if n % 2 == 1:
                res = res * x
            # 奇数
            # 乘上一个x,让 n 变成奇数
            res *= x
            n = n/2
        return res