'''给你一个字符串 s，找到 s 中最长的回文子串。'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        # 把字符串中每个字母均视为回文子串的中心
        # 长度为偶数时中心有两个字母，长度为奇数时中心有一个字母
        for i in range(len(s)):
            s1 = self.helper(s, i, i)   # 奇数情况
            if len(s1) > len(ans):    
                ans = s1
            
            s2 = self.helper(s, i, i+1) # 偶数情况
            if len(s2) > len(ans):
                ans = s2
        return ans

    def helper(self, s, l, r):          
        while l>=0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]                 # 在临界位置还进行了一轮扩展，
                                        # 故左端缩减1，右端本身就大1，故不需要缩减
