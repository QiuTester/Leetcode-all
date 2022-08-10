'''给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 二分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:                          # 左闭右闭形式
            mid = (low+high) >> 1
            if nums[mid] < target: low = mid + 1    # 都是缩小长度
            elif nums[mid] > target: high = mid - 1
            else: return mid
        return -1
