# 这种方法没问题，但是会超时
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = [False] * n
#         dp[0] = True
#         for i in range(n):
#             # 注意审题，每个元素代表的是可以跳跃的最大长度，不是只能跳几步
#             if dp[i]:
#                 end = min(i+nums[i]+1,n)
#                 for j in range(i,end):
#                     dp[j] = True
#         return dp[-1]

# https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
# 这种方法相比于上个方法 ，在当前位置不需要更新所有num[i]的值，只需要更新最远的位置，时间复杂度提升了许多，只需要O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 能到达的最远位置
        end = 0
        # i是当前位置
        for i in range(len(nums)):
            # end >= i 说明 这个位置可以到达
            # i+nums[i] > end 说明能到到的最远距离更新了
            if end>=i and i+nums[i] > end:
                end = i + nums[i]
        # 看最后最远的距离是不是比 len(num) - 1 大
        return end >= len(nums) -1