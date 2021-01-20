"""
【题目】
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].

【题目大意】
在数组中找到 2 个数之和等于给定值的两个数字，结果返回 2 个数字在数组中的下标。（假设只有两个数相加等于给定值，且一个数不能使用两次）

【解题思路】
这道题最优的做法时间复杂度是 O(n)。
顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，如果找到了，直接返回 2 个数字的下标即可。如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。

【注意事项】
1、一个数不能用两次
2、数组可以出现相同的数字
"""
import random


def two_sum_1(nums, target):
    for i in nums:
        if target - i in nums[nums.index(i)+1:]:
            index_1 = nums.index(i)
            # 题目中没有说列表中不能出现相同数字，如果刚好出现两个相同的数字等于target，此时如果没有移除该值，第二个值的索引值就获取不到
            nums.remove(i)
            index_2 = nums.index(target - i) + 1
            return [index_1, index_2]
    return None


def two_sum_2(nums, target):
    for i in nums:
        index_1 = nums.index(i)
        # 题目中没有说列表中不能出现相同数字，如果刚好出现两个相同的数字等于target，此时如果没有移除该值，第二个值的索引值就获取不到
        nums.remove(i)

        if target - i in nums:
            index_2 = nums.index(target - i) + 1
            return [index_1, index_2]

        nums.insert(index_1, i)
    return None


l1 = [random.randint(1, 10) for i in range(10)]
l2 = l1.copy()
t = random.randint(4, 8)

print(f"nums:{l1}")
print(f"target:{t}")
print(two_sum_1(l1, t))
print(two_sum_2(l2, t))




