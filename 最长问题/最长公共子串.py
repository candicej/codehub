# 最长公共子串

# 子问题是 dp[i][j] :表示从0开始到字符串A的弟i个字符串和字符串B的第j个字符串的最长公共子序列
# 递推公式就是：
# 初始条件 如果i= 0 或者 j = 0 dp[i][j] = 0
# 如果A[i]和B[j] 相等 dp[i][j] = dp[i-1][j-1] + 1
# 如果A[i]和B[j] 不相等 dp[i][j] = 0 ****注意 这里是和自序列的区别 因为
# 当A[i] != B[j]时，res[i][j]就直接等于0了，因为子串必须连续，且res[i][j] 表示的是以A[i]，B[j]截尾的公共子串的长度

# 那么这道题 最大的值 就不一定是二维数组的最后一个值了，可能是前面的某个dp[][j],需要设置一个res 变量 存储最大值

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    # 创建（m+1)*(n+1)表格的原因是 当i=0 时，str1[0:i] 为空，空字符串和任何字符串的最长公共子序列的长度都是 0, 画表时需要多画一行

    dp = [[0]*(n+1) for j in range(m+1)]
    res = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
    return res

print(lcs("helloworld", "loop"))