'''你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# 二分（模版2）
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n 
        while left < right:                           # 开始位置一定返回是False，目标在于找到第一个为True的下标 
            mid = (left+right) >> 1           
            if not isBadVersion(mid): left = mid + 1  # 当前点仍然为False，继续向右找
            else: right = mid                         # 当前点满足，但不一定是第一个True，保留当前点再继续向左找（最后会返回单一值left==right）
        return left
