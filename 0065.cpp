'''写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。'''

# 位运算（递归）
class Solution {
public:
    int add(int a, int b) {
        if(b == 0) return a;                          # n为非进位和（异或运算），c作为进位（与运算），将s=a+b转换为s=n+c
        return add(a ^ b, (unsigned)(a & b) << 1);    # 递归求n和c，直到找到进位c为0的位置作为出口，此时s=n+0=n=a
    }
};
