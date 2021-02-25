'''
Date: 2021-02-24 19:09:21
LastEditTime: 2021-02-25 23:25:15
Author: Ye-P
Descripttion: 二叉树
'''
from typing import Optional
import binarytree
import random
t = binarytree.tree(height=3, is_perfect=True)
# print(t)


class Node(object):
    def __init__(self, value, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        super().__init__()
        self.data = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return super().__str__()


def build_random_tree(height: int = 3, is_prefect=False) -> Optional[Node]:
    max_node_len = 2**height-1
    values = list(range(max_node_len))
    random.shuffle(values)
    return build_tree(values=values, is_prefect=is_prefect)


def build_prefecet_tree(nodes: list):
    for index, node in enumerate(nodes):
        parent_node = nodes[index//2]
        if parent_node == None:
            raise Exception('parent node not find')
        if index % 2 == 0:
            setattr(parent_node, 'right', node)
        else:
            setattr(parent_node, 'left', node)
    return nodes[0]


def build_normal_tree(nodes: list, height: int):
    if len(nodes) > (2**height-1):
        raise Exception('can not build tree,because nodes > 2**height-1')
    # todo
    pass


def build_tree(values: list, is_prefect=True, height: int = 3):
    if values == None:
        return None
    elif len(values) == 0:
        return None
    elif is_prefect:
        nodes = list(map(lambda v: Node(v), values))
        return build_prefecet_tree(nodes=nodes)
    else:
        # todo
        pass


atree = build_random_tree()
print(atree)
