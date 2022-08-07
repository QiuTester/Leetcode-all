''' 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 '''


# 排序
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda x:x[0]) # 以左端点大小来排序
        for start, end in intervals:
            if not ans or ans[-1][1] < start:  # 若ans为空或ans最右端点小于当前intervals输入左端点，直接将当前区间append到ans上
                ans.append([start, end])
            else:                              # 若ans最右端点大于/等于当前intervals输入左端点，判断当前end与ans最右谁更大并更新
                ans[-1][1] = max(ans[-1][1], end)  
        return ans
