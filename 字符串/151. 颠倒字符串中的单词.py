# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # 先将一个字符串 分割成若干个子字符串  ['the', 'sky', 'is', 'blue']
#         # 反转 <list_reverseiterator object at 0x000001983B25A8D0>
#         # 使用' '连起来
#         return ' '.join(reversed(s.split()))

# 依此遍历
# https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/pythonshuang-zhi-zhen-lie-biao-by-ryanl-tkof/
# 1.先将字符串两边的空格去掉，可以自己编一个程序，也很简单，这里直接使用strip函数
# 2.利用快慢指针进行遍历字符串，当移动到空格时，在结果列表中append此时i到j的单词，此后，将i移动到下一个单词（或者空格）的首位，继续对j进行遍历
# 3.如果此时j又移动到空格，同时i=j的情况下，要对i和j同时加1，此步是为了去除多余空格

class Solution:
    def reverseWords(self, s: str) -> str:
        i = j = 0
        l = []
        s = s.strip(' ')
        while j < len(s):
            if s[j] == ' ' and i != j:
                l.append(s[i:j])
                i = j + 1
            elif s[j] == ' ' and i == j:
                i += 1
            if j == len(s) - 1:
                l.append(s[i:j+1])
            j += 1
        return ' '.join(l[::-1])

