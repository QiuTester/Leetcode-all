'''峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 二分（模版2）
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:                            # nums[-1]=负无穷，开始一定是上坡，目标在于找到第一个下坡点
            mid = (left+right) >> 1                      
            if nums[mid] < nums[mid+1]: left = mid + 1 # 当前点仍然为上坡，继续向右找  
            else: right = mid                          # 找到了下坡点，但要找到唯一（第一个满足）的那一个点，故将当前点包含在内再继续向左找（最后返回唯一值left==right）
        return left
