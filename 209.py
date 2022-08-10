'''给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 滑动窗口双指针
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast, ans = 0, 0, len(nums)+1
        sums = 0
        while fast < len(nums):
            sums += nums[fast]                  # 快指针遍历数组，求元素值总和
            while sums >= target:               # 当总和大于目标时，依次缩短慢指针
                ans = min(ans, fast-slow+1)     # 直到总和小于目标值
                sums -= nums[slow];
                slow += 1
            fast += 1                           # 先利用慢指针缩短长度再继续便利
        return 0 if ans==len(nums)+1 else ans
