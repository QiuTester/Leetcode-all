'''给你一个整数数组 nums ，请计算数组的 中心下标 。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-pivot-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)     # 先得到数组所有元素之和 
        left = 0
        for i in range(0, len(nums)):
            if left*2 + nums[i] == sums: # 若当前元素的左侧所有元素之和的两倍等于（总和-当前元素），满足左侧等于右侧
                return i
            else:
                left += nums[i]         # 更新左侧元素之和
        return -1
