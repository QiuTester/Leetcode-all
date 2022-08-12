'''给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-k-closest-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 二分（模版2）（模版3太难用了）
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k           
        while left < right:                     # 可以理解为从开始不断向右找区间的最左端点（与x的差值最小）
            mid = (left+right) >> 1             # 每次循环假设mid为最左端点
            if x - arr[mid] > arr[mid+k] - x:   # 此时mid不满足，继续向右找
                left = mid + 1   
            else: right = mid                   # mid满足最左端点（与x差最小），但不能确定是第一个满足点
                                                # 继续向左找，直到满足left==right跳出循环
        return arr[left:left+k]                 # 直接返回最左端点以及其右边k-1个元素
