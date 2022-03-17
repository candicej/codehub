# 二分法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums:
            return [-1,-1]
        l,r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                left, right = mid,mid
                # 往前往后查找
                while left-1 >= l and nums[left-1]==target:
                    left -= 1
                while right+1 <= r and nums[right+1]==target:
                    right += 1
                # 返回结果
                return [left,right]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return [-1,-1]