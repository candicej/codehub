# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # 队列 如果有重复的就把她清空
        stk = []

        # 记录整个过程中的队列里的元素的最大量
        max_len = 0
        for i in range(n):
            while stk and s[i] in stk:
                stk.pop(0)
            stk.append(s[i])
            max_len = max(max_len, len(stk))
        return max_len