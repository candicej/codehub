
# 思路就是 从后往左 找到第一个比较小的数字 ： nums[i] < nums[i+1]
# 再从后往前找一个 比 nums[i]大的nums[j], 交换他们的顺序
# 比如 456321 i= 1 j= 2 交换 变成 465321
# 然后将 nums[i+1:n] 反转 整个数组就是 下一个排列了

# 特殊情况的话 ， i = -1 直接全部反转 ok的

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        size = len(nums)

        i = size - 2
        j = size - 1

        # 从后往前找 第一个比较小的数字
        # 这里得有 等于，因为要找第一个比较小的数，不然就会找到相同的数字
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 从后往前 找第一个比 nums[i]大的数字
        # 这里 必须是 i>= 0
        # 因为如果 i 是最开头的这个数，那么 i = -1, 就不需要进行交换，直接进行下一步，翻转数组就可以了。
        if i >= 0:
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # 交换
            nums[i], nums[j] = nums[j], nums[i]

        # 对 nums[i+1:n] 反过来 后半部分就是 从小到大有序的了
        nums[i + 1:size] = reversed(nums[i + 1:size])