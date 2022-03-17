def search(nums, target) -> int:
    if not nums:
        return -1
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 左半部分有序
        if nums[mid] >= nums[left]:
            # 左边取等号是因为 有可能是最左边的元素，但是前面已经判断了nums[mid] == target
            if nums[left] <= target < nums[mid]:
                # 说明 在左半部分，改变right的值
                right = mid - 1
            # 说明 在右半部分，改变left的值
            else:
                left = mid + 1
        # 右半部分有序
        else:
            # 改变left
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            # 改变right
            else:
                right = mid - 1
    return -1
s = search([8,9,10,11,1,2,3,4,5,6,7], 1)
print(s)