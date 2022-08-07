'''有一个 单线程 CPU 正在运行一个含有 n 道函数的程序。每道函数都有一个位于  0 和 n-1 之间的唯一标识符。

函数调用 存储在一个 调用栈 上 ：当一个函数调用开始时，它的标识符将会推入栈中。而当一个函数调用结束时，它的标识符将会从栈中弹出。标识符位于栈顶的函数是 当前正在执行的函数 。每当一个函数开始或者结束时，将会记录一条日志，包括函数标识符、是开始还是结束、以及相应的时间戳。

给你一个由日志组成的列表 logs ，其中 logs[i] 表示第 i 条日志消息，该消息是一个按 "{function_id}:{"start" | "end"}:{timestamp}" 进行格式化的字符串。例如，"0:start:3" 意味着标识符为 0 的函数调用在时间戳 3 的 起始开始执行 ；而 "1:end:2" 意味着标识符为 1 的函数调用在时间戳 2 的 末尾结束执行。注意，函数可以 调用多次，可能存在递归调用 。

函数的 独占时间 定义是在这个函数在程序所有函数调用中执行时间的总和，调用其他函数花费的时间不算该函数的独占时间。例如，如果一个函数被调用两次，一次调用执行 2 单位时间，另一次调用执行 1 单位时间，那么该函数的 独占时间 为 2 + 1 = 3 。

以数组形式返回每个函数的 独占时间 ，其中第 i 个下标对应的值表示标识符 i 的函数的独占时间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/exclusive-time-of-functions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 栈模拟
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            idx, tp, timestamp = log.split(':')      # 分割log
            idx, timestamp = int(idx), int(timestamp)  

            if tp[0] == 's':                        # 入栈时（start）
                if stack:   # 栈内有正在执行的函数时，暂停并记录其独占时长，然后记录暂停时间戳
                    ans[stack[-1][0]] += timestamp - stack[-1][1]
                    stack[-1][1] = timestamp         # stack[-1][0]:栈顶id；
                                                     # stackstack[-1][1]:栈顶start/end时间戳
                stack.append([idx, timestamp])        # 入栈

            else:                                    # 出栈时（end）
                idl, out_timestamp = stack.pop()     # 记录出栈函数的id和时间戳
                ans[idl] += timestamp - out_timestamp + 1  
                # 记录出栈对应函数独占时长 = 出栈时间戳-出栈函数暂停时间戳+1（出栈本身也算1单位时间）
                if stack:                            # 更新栈顶时间戳（+1是因为出栈本身也算1单位时间）
                    stack[-1][1] = timestamp + 1
        return ans
