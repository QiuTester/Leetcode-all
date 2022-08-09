'''给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 ’n 的 min(ai, bi) 总和最大。

返回该 最大总和 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/array-partition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()               # 先排序，再取偶数位置之和（尽可能把大的数放在一起，并取其中较小的数）
        sums = sum(nums[::2])     # 减少内存消耗
        return sums
