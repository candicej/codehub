# 进阶版 300. 最长递增子序列

# 连续的只需要和前面的一个比较就可以了
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        max_len = 1
        for i in range(1,size):
            # 状态转移
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                max_len = max(dp[i], max_len)
        return max_len