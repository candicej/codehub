# 参考 https://leetcode-cn.com/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-dong-tai-gu-p7uk/ 写的很清晰
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 特例判断
        if n == 1:
            return s
        # 二维表格
        dp = [[False] * n for _ in range(n)]
        # 初始长度为1，这样万一不存在回文，就返回第一个值（初始条件设置的时候一定要考虑输出）
        start = 0
        max_len = 1

        # 从左到右，从上到下填表，且只填右上部分
        for j in range(1,n):
            for i in range(0,j):
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = j-i+1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        cur_len = j-i+1
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start+max_len]
