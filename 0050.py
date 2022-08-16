'''实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。'''

# 快速幂（递归）
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(x, N):
            if not N: return 1.0
            y = quickPow(x, N >> 1)                                 # 将幂次不断拆分，直到N == 0返回1，再回溯
            return y * y if not N % 2 else y * y * x                # 当幂次为奇数时还要多乘一次底数

        return quickPow(x, n) if n >= 0 else 1.0 / quickPow(x, -n)  # 判断幂次是正数还是负数
