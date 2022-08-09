'''给你一个字符串 s ，颠倒字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    # method 1
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1]) # 倒叙遍历分割后的字符串，并以‘ ’为间隔依次插入返回
      
    # method 2   
    def reverseWords(self, s: str) -> str:
        word, split_word = "", []
        for i in s:                      # 遍历字符串，当前元素不为空格时加到word上；为空格时append更新后清空word
            if i != " ": word += i
            elif word:
                split_word.append(word)
                word = ""
        if word: split_word.append(word) # 当字符串结尾不为空格时，最后一个单词需要在循环结束后再单独append
        return " ".join(split_word[::-1]) 
