'''输入两个链表，找出它们的第一个公共节点.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        NodeA, NodeB = headA, headB
        while NodeA != NodeB:  # 两个指针分别遍历列表，若遍历到自身尾节点时仍未相遇，则从对方的头节点再次开始遍历，直到两者相遇。
            NodeA = NodeA.next if NodeA else headB    # 三目运算符，若NodeA==NULL则从headB开始遍历
            NodeB = NodeB.next if NodeB else headA    # 使用NodeA而不是NodeA.next代替列表不相交的特殊情况
        return NodeA                                  # 当两列表没有交集时，NodeA和NodeB终究会同时指向NULL，此时循环依然会结束，并且返回null
