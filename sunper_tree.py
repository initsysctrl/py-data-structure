'''
Date: 2021-03-08 07:07:17
LastEditTime: 2021-03-08 10:48:09
Author: Ye-P
Descripttion: 二叉树的例子
'''


from typing import List


class TNode():
    """[定义二叉树节点]
    """

    def __init__(self, data, left=None, right=None) -> None:
        """[summary]

        Arguments:
            data {[type]} -- [数据]
            left {[type]} -- [左节点]
            right {[type]} -- [右节点]
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        a = self.left.__str__() if self.left != None else None
        b = self.right.__str__() if self.right != None else None
        return {self.data: [a, b]}.__str__()


def count_node(root: TNode):
    """统计二叉树的全部节点数量"""
    # base case
    if root == None:
        return 0
    return count_node(root.left)+count_node(root.right)+1


def revert_tree(root: TNode):
    """翻转二叉树的孩子节点"""
    # base case
    if root == None:
        return
    # logic
    root.left, root.right = root.right, root.left
    revert_tree(root.left)
    revert_tree(root.right)
    return root


def preorder(root: TNode):
    """前序遍历二叉树"""
    buff = []

    def f(root):
        if root == None:
            buff.append('#')
            return
        buff.append(root.data)
        f(root.left)
        f(root.right)
    f(root=root)
    return buff


def deserialize(arr: list):
    if len(arr) == 0:
        return
    val = arr.pop(0)
    root = None
    if val != '#':
        root = TNode(val)
        root.left = deserialize(arr)
        root.right = deserialize(arr)
    return root


def build_max_tree(arr: List[int]):
    """把无重复的数组构建成最大二叉树"""
    """"""
    if len(arr) == 0:
        return
    max_value = max(arr)
    root = TNode(max_value, None, None)
    i = arr.index(max_value)
    left_arr = arr[0:i]
    right_arr = arr[i+1:]
    root.left = build_max_tree(left_arr)
    root.right = build_max_tree(right_arr)
    return root


def find_repeat(root: TNode):
    """寻找最大二叉树"""
    buff = []
    meno = []

    def f(root):
        if root == None:
            return
        ls = preorder(root)
        if ls not in buff:
            buff.append(ls)
        else:
            meno.append(root.data)
        f(root.left)
        f(root.right)
    f(root=root)
    return set(meno)


t4 = TNode(4, None, None)
t5 = TNode(5, None, None)
t2 = TNode(2, t4, t5)
t3 = TNode(3, None, None)

root = TNode(1, t2, t3)
print(root)
print(preorder(root))

root = build_max_tree([3, 2, 1, 6, 0, 5])
print(root)
# 寻找重复子树
a = TNode(1)
b = TNode(2)
c = TNode(2)
d = TNode(3)
e = TNode(4)
f = TNode(4)
g = TNode(4)
a.left = b
a.right = d
b.left = e
d.left = c
d.right = f
c.left = g
print(preorder(root))
print(find_repeat(root=a))
print(deserialize([6, 3, '#', 2, '#', 1, '#', '#', 5, 0, '#', '#', '#']))
