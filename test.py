'''
Date: 2021-03-08 11:27:28
LastEditTime: 2021-03-08 12:19:39
Author: Ye-P
Descripttion: 
'''


def common(arr: list):
    """求最大公约数"""
    min_num = min(arr)
    print(sorted(range(1, min_num+1), reverse=True))
    for i in sorted(range(1, min_num+1), reverse=True):
        flags = [x % i for x in arr]
        if not any(flags):
            return i
    return None


c = common([16, 32, 40, 72])
print(c)


def handle_num(arr: list):
    """
    去掉连续出现次数大于等于三次的数
    例如输入[1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5]
    输出：[1, 1, 2, 2, 3, 3, 4, 4, 5]

    """
    buff = []
    if len(arr) <= 2:
        return arr
    for i, e in enumerate(arr):
        if len(buff) < 2:
            buff.append(e)
            continue
        if e == buff[-1] and e == buff[-2]:
            continue
        buff.append(e)
    return buff


a = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5]
print(a)
arr = handle_num(a)
print(arr)
