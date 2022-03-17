# https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
        dp = [[0]*(n+1) for _ in range(m+1)]

        # 初始化 第0行和第0列
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                # 如果这一位相等，那就不用修改，和上一次的一样
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
                    # +1 是因为不相等需要操作一次
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]