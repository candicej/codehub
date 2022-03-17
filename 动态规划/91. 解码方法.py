def numDecodings(s) -> int:
    n = len(s)
    # f[i] 表示字符串 ss 的前 ii 个字符 s[1..i]s[1..i] 的解码方法数
    # f[0] = 1 是因为空字符串可以有 11 种解码方法，解码出一个空字符串。
    f = [1] + [0] * n

    # 注意 字符串的下标是从 0开始，所以需要s[i-1]
    for i in range(1, n + 1):
        # 只要s[i-1] != 0 就可以满足解码成某一种形式
        # 如果 s[i-1] = 0 说明当前的字符不能只有一个进行编码，所以只能 等于f[i-2]
        if s[i - 1] != '0':
            f[i] = f[i - 1]
        # 选取两个字符作为当前编码方式
        if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            f[i] = f[i - 2]
    return f[n]
a = numDecodings("110")
