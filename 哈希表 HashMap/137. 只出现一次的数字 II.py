# 简单方法和 169 题一样
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        # 这里可以用 k in dic 也可以是 k in dic.keys()
        for k in dic.keys():
            if dic[k] == 1:
                return k