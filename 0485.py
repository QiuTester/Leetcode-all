'''给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。'''

# 双指针
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        ans = 0
        for fast in range(len(nums)):
            if not nums[fast]:                     # 快指针指向0时，更新ans和慢指针          
                ans = max(fast-slow, ans)          # ans正常更新  
                slow = fast + 1                    # ！慢指针更新位置为快指针当前位置下一位

            if nums[fast] and fast == len(nums)-1: # 当数组的末尾为1时，遍历来不及更新就结束，故分类讨论
                ans = max(fast-slow+1, ans)        # 快指针当前所指元素也是1，因此相比ans正常更新要+1
        return ans
