# https://leetcode-cn.com/problems/single-number-iii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-8/
# 首先异或得到 只存在一次的两个数，
# 我们构造一个数，把我们要找的那两个数字二进制不同的那一位写成 1，其它位都写 0，也就是 0...0100...000 的形式。
# 然后把构造出来的数和数组中的数字相与，如果结果是 0，那就意味着这个数属于当前位为 0 的一类。否则的话，就意味着这个数属于当前位为 1 的一类

# [1,2,1,3,2,5]
# 1 = 001
# 2 = 010
# 1 = 001
# 3 = 011
# 2 = 010
# 5 = 101
# 把上边所有的数字异或，最后得到的结果就是 3 ^ 5 = 6 (110)
#
# 然后对 110 调用 Integer.highestOneBit 方法就得到 100, 我们通过倒数第三位将原数组分类
# 倒数第三位为 0 的组
# 1 = 001
# 2 = 010
# 1 = 001
# 3 = 011
# 2 = 010
# 倒数第三位为 1 的组
# 5 = 101
# 对两组数据，各自异或就ok

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = nums[0]
        for i in range(1,len(nums)):
            res = res ^ nums[i]
        # 可以用来获取某个二进制数的LowBit
        lsb = res & -res
        # 用来找最后的值得
        a = 0
        b = 0
        for i in range(len(nums)):
            # 当前是1 的组 ，组内异或
            if lsb & nums[i]:
                a = a ^ nums[i]
            # 当前是0 的组， 组内异或
            else:
                b = b ^ nums[i]
        return a,b



