# LCS
# 利用动态规划
# 因为有两个字符串，每个字符串的长度分别是m,n,所以是一个二维动态转移

# 子问题是 dp[i][j] :表示从0开始到字符串A的弟i个字符串和字符串B的第j个字符串的最长公共子序列
# 递推公式就是：
# 初始条件 如果i= 0 或者 j = 0 dp[i][j] = 0
# 如果A[i]和B[j] 相等 dp[i][j] = dp[i-1][j-1] + 1
# 如果A[i]和B[j] 不相等 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# https://blog.csdn.net/ggdhs/article/details/90713154 写的很清楚

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    # 创建（m+1)*(n+1)表格的原因是 当i=0 时，str1[0:i] 为空，空字符串和任何字符串的最长公共子序列的长度都是 0, 画表时需要多画一行

    dp = [[0]*(n+1) for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(lcs("helloworld", "loop"))
