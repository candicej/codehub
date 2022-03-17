# 暴力搜索 法
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1

# 方法二 利用局部有序的特点，进行局部的二分查找
# 查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
# 并根据有序的那个部分确定我们该如何改变二分查找的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        left, right = 0, n-1
        while left<= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            # 左半部分有序
            if nums[mid] >= nums[left]:
                # 左边取等号是因为 有可能是最左边的元素，但是前面已经判断了nums[mid] == target
                if nums[left] <= target < nums[mid]:
                    # 说明左半部分，改变right的值
                    right = mid -1
                # 说明 在右半部分，改变left的值
                else:
                    left = mid + 1
            # 右半部分有序 根据右部分更改left或者right 的值
            else:
                # 改变left
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # 改变right
                else:
                    right = mid - 1
        return -1