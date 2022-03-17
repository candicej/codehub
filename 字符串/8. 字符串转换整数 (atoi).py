# 方法一 正则匹配 寻找符号条件的数
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         INT_MAX = 2147483647
#         INT_MIN = -2147483648
#         str = str.lstrip()      #清除左边多余的空格
#         num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
#         num = num_re.findall(str)   #查找匹配的内容
#         num = int(*num) #由于返回的是个列表，解包并且转换成整数
#         return max(min(num,INT_MAX),INT_MIN)    #返回值

# 正则表达式
# (r'^[\+\-]?\d+') 含义：
# ^ 表示匹配字符串开头，我们匹配的就是 '+'  '-'  号
# [] 表示匹配包含的任一字符，比如[0-9]就是匹配数字字符 0 - 9 中的一个
# ? 表示前面一个字符出现零次或者一次，这里用 ? 是因为 '+' 号可以省略
# \d 表示一个数字 0 - 9 范围
# + 表示前面一个字符出现一次或者多次，\d+ 合一起就能匹配一连串数字了

# 方法二 常规处理方法
class Solution:
    def myAtoi(self, s: str) -> int:
        # 去掉空格
        s = s.strip()
        # 如果字符串是 "" 返回0
        if not s:
            return 0
        # 存储最终结果
        res = 0
        # 符号位
        flag = 1
        if s[0] == "+":
            flag = 1
        elif s[0] == "-":
            flag = -1
        elif s[0].isdigit():
            res = int(s[0])
        else:
            return 0

        # 开始遍历数字
        for i in range(1, len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
        res *= flag
        # 判断是否越界
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < -2 ** 31:
            res = -2 ** 31

        return res