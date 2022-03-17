class Solution:
    def rob(self, nums: List[int]) -> int:

        def robhouse(left, right):
            # 直接使用滚动数组节省时间
            fi = nums[left]
            se = max(nums[left], nums[left + 1])
            for i in range(left + 2, right):
                fi, se = se, max(fi + nums[i], se)
            return se

        n = len(nums)
        # 首先进行特例判断，只有一个或者两个的情况
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # 将问题转化成 不偷第一间 和不偷最后一间两个子问题，选择较大的那一个
        res = max(robhouse(0, n - 1), robhouse(1, n))
        return res
