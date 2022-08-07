'''给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。

如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/string-matching-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 遍历
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, x in enumerate(words):         # enumerate:遍历words，i代表元素序号，x代表元素；enumerate(words, n)其中n代表i从多少序号开始
            for l, y in enumerate(words):
                if x != y and x in y:         # 若x和y不相等且y包含x，可得x满足条件
                    ans.append(x)
                    break                     # 防止多个元素满足导致重复append
        return ans
