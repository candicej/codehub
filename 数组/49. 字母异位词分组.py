# 牛逼，根据异位词的字母构成是一样的，排序，作为键，然后把答案作为值（列表）存进去
# 由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的键。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        res = []
        for st in strs:
            # sorted(st) 是 ['3','4','5'] 得用join函数 连起来变成 '345'
            # 哈希表的键
            key = "".join(sorted(st))
            # 出现过，
            if key in dic:
                # 一个间可以对应一个列表 ！！{'aet': ['eat', 'tea']}
                dic[key].append(st)
            # 没出现过
            else:
                dic[key] = [st]
        for val in dic.values():
            res.append(val)

        return res

