''' 整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 依然是二分，只不过利用一些题目条件
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:                                      # 数组分为左右两段区间，k~n-1递增和0～k-1递增
            mid = (left+right) >> 1                               # 由此可以得知，num[0]<num[len(num)-1]
            if nums[mid] == target: return mid                    # 最大值在数组中间的某个位置

            if nums[mid] >= nums[left]:                           # 此时mid在数组左半（递增）区间                       
                if nums[mid] > target and nums[left] <= target:     
                    right = mid - 1                               # 相当于target在left和mid之间的位置，缩短right
                else: left = mid + 1                              # 不满足则target在mid和right之间，缩短left
            
            else:                                                 # 此时mid在数组右半（递增）区间
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1                                # 与上述同理
                else: right = mid - 1
        return -1
