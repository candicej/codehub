class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        n = len(s)
        flag = 0
        for i in range(n-1,-1,-1):
            if s[i]!= " ":
                count += 1
                flag = 1
            if s[i] == " " and flag == 1:
                return count
        return count
