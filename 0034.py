'''给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 二分（模版3）
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        left, right = 0, len(nums)-1
        while left+1 < right:                  # 先找最左位置
            mid = (left+right) >> 1
            if nums[mid] < target: left = mid  # 关键点在于等号的选择
            else: right = mid                  # 此时等号选在右邻居，以右邻居检索满足target的值
        
        if nums[left] == target: l = left      # 模版3跳出时left和right为两个不同的值
        elif nums[right] == target: l = right  # 此时可能是left满足也可能是right满足
        else: return [-1, -1]                  # 因为找的是最左位置，优先判断左邻居是否满足 
                                               # 若都不满足返回[-1, -1]

        left, right = 0, len(nums)-1           # 再找最右位置
        while left+1 < right:
            mid = (left+right) >> 1
            if nums[mid] <= target: left = mid # 等号选在左邻居，以左邻居检索满足值
            else: right = mid
        
        if nums[right] == target:return [l, right] # 优先判断右邻居是否满足
        else: return [l, left]
