'''给你一个整数 n ，表示一个国家里的城市数目。城市编号为 0 到 n - 1 。

给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] 表示城市 ai 和 bi 之间有一条 双向 道路。

你需要给每个城市安排一个从 1 到 n 之间的整数值，且每个值只能被使用 一次 。道路的 重要性 定义为这条道路连接的两座城市数值 之和 。

请你返回在最优安排下，所有道路重要性 之和 最大 为多少。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-total-importance-of-roads
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 贪心
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        maps = n * [0]     # 初始化
        for a, b in roads: # 每个城市通有道路的数量
            maps[a] += 1
            maps[b] += 1
        maps.sort()        # 由小到大排序
        return sum(i * j for i, j in enumerate(maps, 1))   
        # 通有越多道路的城市被安排的值越大，重要性之和等于1*（最少道路城市）+2*（第二少道路城市）+·····+n*（最多道路城市）
