"""
【题目】
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

【题目大意】
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将表示的两个数相加返回值用一个新的链表逆序存储。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

【解题思路】
这道题最优的做法时间复杂度是 O(n)，n为较长的链表节点数。
两个链表的头节点刚好对应逆序后整数的个位数，如果从头节点开始提取两个链表的每个节点的确切值并将它们相加，则刚好符合加法的计算规则（个位与个位相加，十位与十位相加。。。）
按提取顺序，将每个节点确切值相加后的个位，以尾插法的方式，插入到一个新链表中，新链表刚好是逆序的两个整数相加后的逆序链表。

【注意事项】
1、各位数进制问题
2、需要先构建链表结构！
"""
import random


class Node(object):
    """构造单链表的节点"""
    def __init__(self, value):
        # 元素域
        self.value = value
        # 链接域
        self.next = None


class ListNode(object):
    """构造单链表"""
    def __init__(self):
        self.__head = None

    def __len__(self):
        # 游标，用来遍历链表
        cur = self.__head
        # 记录遍历次数
        count = 0
        # 当前节点为None则说明已经遍历完毕
        while cur:
            count += 1
            cur = cur.next
        return count

    def append(self, value):
        """在链表的最后插值"""
        node = Node(value)
        cur = self.__head
        if self.__head is None:
            self.__head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    def get_nodes(self, var_name):
        """获取链表对象"""
        cur = self.__head
        s_ln = ''
        while cur:
            s_ln += str(cur.value) + ' > '
            cur = cur.next
        print(f"{var_name}: {s_ln}")
        return self.__head


def create_list_node(var_name):
    """生成随机链表"""
    l_len = random.randint(1, 6)
    l_nums = [random.randint(1, 9) for i in range(l_len)]
    ln = ListNode()
    for i in l_nums:
        ln.append(i)
    return ln.get_nodes(var_name)


def sum_list_node(ln1, ln2):
    n1, n2, c, new_ln = 0, 0, 0, ListNode()
    """
    参数说明
    n1: ln1节点的确切值
    n2: ln2节点的确切值
    c: 相加后十位数上的值
    new_ln: 相加后生成的新的链表
    """
    while ln1 or ln2 or c != 0:
        if ln1:
            n1 = ln1.value
            ln1 = ln1.next
        else:
            n1 = 0

        if ln2:
            n2 = ln2.value
            ln2 = ln2.next
        else:
            n2 = 0

        # 提取相加大于10的十位数值
        s = n1 + n2 + c
        c = s // 10
        new_ln.append(s % 10)
    return new_ln


l1 = create_list_node("l1")
l2 = create_list_node("l2")
l3 = sum_list_node(l1, l2).get_nodes("l3")
