'''给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 二分法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:      # 左闭右闭[left, right]形式
            mid = (left + right) >> 1
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid - 1
            else: left = mid + 1
        return right + 1
''' 若‘while left < right’ 则为左闭右开[left, right)形式
改成：  if nums[mid] == target: return mid
       elif nums[mid] > target: right = mid
       else: left = mid + 1
   return right               '''

      
