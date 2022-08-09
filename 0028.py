'''实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# KMP：字符串匹配算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        Next = self.getNext(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j] or j < 0:    # j<0时j=-1，模式串从头开始匹配
                if j == len(needle)-1: return i - j
                i+=1; j+=1
            else: j = Next[j]                        # 对位不相等，主串(haystack)不动
        return -1                                    # 从模式串下标为next[j]处继续匹配
    
    def getNext(self, needle):                       # 得到next数组
        Next, j, k = [0]*len(needle), 0, -1          
        Next[j] = k
        while j < len(Next)-1:                       # 当p_k=p_j时，next[j+1] = next[j]+1 = k+1
            if k == -1 or needle[j] == needle[k]:    # 当p_k!=p_j时，不断递归索引k=next[k]，
                k+=1; j+=1                           # 直到满足p_next[k]=p_j或p_next[next[...]]=0,
                Next[j] = k                          # 此时最大公共前后缀为0，next[j+1] = 0
            else: k = Next[k]
        return Next
