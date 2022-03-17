# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 这道题 和小彭讨论了好久
# 他没搞明白，但是我明白了哈哈哈
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            #生成1-7
            row = rand7()
            col = rand7()

            # (row-1)* 7 生成 0 7 14 21 ...
            # col 生成 1 2 3 4 5 6 7
            # 两个相加就可以等概率生成 1- 49
            # 我们只取前40个数字，每个数字出现概率都是4/49
            idx = (row-1)* 7 + col
            if idx<= 40:
                # idx - 1 是 0 -39 那么对十取余 就是 0-9 加一就是 1 -10
                return 1 + (idx-1)%10
