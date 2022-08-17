'''在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。'''

# 归并排序、双指针、递归分治
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left, right):
            # 划分的出口
            if left >= right: return 0
            
            # 递归划分（二分）
            mid = (left+right) >> 1                                 # 利用递归，把原数组不断划分为左右两个子数组（子数组最小长度为1）
            ans = merge_sort(left, mid) + merge_sort(mid+1, right)  # 最后每段数组会返回其左右子数组满足逆序对的元素数量，相加即为ans最终值
            
            # 合并（回溯）求解
            amp[left : right+1] = nums[left : right+1]    # 储存划分后的原始数组
            i, j = left, mid+1                            # 双指针i和j分别指向数组的开头和中间，把数组划分为了左右两个子数组
            for k in range(left, right+1):
                if i == mid + 1:                          # 当左指针指向了末尾，意味着左子数组已经排完了
                    nums[k] = amp[j]                      # 接下来把右子数组剩余的元素依次添加就好
                    j += 1
                    
                elif j == right + 1 or amp[i] <= amp[j]:  # 当右指针指向了末尾，意味着右子数组已经排完了，把左子数组剩余的元素依次添加
                    nums[k] = amp[i]                      # 或者左指针指向的元素小于右指针指向的元素，直接添加左指针指向的元素即可
                    i += 1
                    
                else:                                     # 当左指针指向的元素大于右指针指向的元素时，其后方的所有元素均大于右指针当前指向元素
                    nums[k] = amp[j]                      # 即均满足逆序对，因此ans要加上左子数组当前剩余的所有元素数量（mid+1-i）
                    j += 1                                # 同时添加右指针指向元素
                    ans += mid + 1 - i
                    
            return ans

        amp = [0] * len(nums)
        return merge_sort(0, len(nums)-1)                
