class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                # 删除字典中的某个值
                del dic[nums[i]]
            else:
                dic[nums[i]] = 1
        # 这里可以用 k in dic 也可以是 k in dic.keys()
        res = []
        for k in dic:
            res.append(k)
        return res
