def longestCommonSubsequence(text1, text2):
    # 求出数组长度
    m = len(text1)
    n = len(text2)
    # 创建一个m+1 行 n+1 列的二维数组  默认为0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 按照行主次序计算表项 从左到右计算dp的第一行，然后计算第二行
    # 自底向上
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 如果相等
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 不等
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
a = longestCommonSubsequence(
"abcde",
"acef")
print(a)