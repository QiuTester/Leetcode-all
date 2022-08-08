'''编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):                 # 遍历第一个单词的每一个字母
            for str in strs:                          # 遍历字符串的每一个单词
                if len(str) <= i: return ans          # 超出单词长度 
                if str[i] != strs[0][i]: return ans   # 不相等 
            ans += strs[0][i]                         # 均没有超出长度也相等
        return ans
