''' 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 二分
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while low <= high:                            # 左闭右闭形式
            mid = (low+high) >> 1
            if mid == x / mid: return mid
            elif mid < x / mid: low = mid + 1         # 当前值小于目标值，缩左边
            else: high = mid - 1                      # 大于目标值，缩右边
        return high
