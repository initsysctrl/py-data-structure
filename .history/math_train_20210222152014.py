
'''
Date: 2021-02-15 19:44:11
LastEditTime: 2021-02-22 15:20:14
Author: Ye-P
Descripttion: 小屁孩的乘法表测试题
'''
import math
import random
import time


def test1(t, limit):
    # 乘法 9*9
    n = 1
    while True:
        i = random.randint(1, 10)
        j = random.randint(1, 10)
        print(f"{n}/{limit}问题: {i}*{j}=?")
        time.sleep(t)
        print(f"正确答案 {i}*{j}={i*j}")
        print('--'*10)
        n = n+1
        if n > limit:
            print('测试结束........')
            return


def test2(t, limit):
    # 除法
    n = 1
    while True:
        i = random.randint(1, 10)
        j = random.randint(1, 10)
        print(f"{n}/{limit}问题: {i*j}➗{i}=?")
        time.sleep(t)
        print(f"正确答案 {j}")
        print('--'*10)
        n = n+1
        if n > limit:
            print('测试结束........')
            return


def test3(t, limit):
    # 乘法 与 除法 混合
    n = 1
    while True:
        flag = random.choice([True, False])
        i = random.randint(-10, 10)
        j = random.randint(-10, 10)
        left = '' if i >= 0 else '('
        right = '' if i >= 0 else ')'
        if flag:
            print(f"{n}/{limit}问题:{i*j}➗{left}{i}{right}=?")
            time.sleep(t)
            if i == 0:
                print(f"分母为0，无解")
            else:
                print(f"正确答案 {j}")

        else:
            print(f"{n}/{limit}问题: {j}✖️{left}{i}{right}=?")
            time.sleep(t)
            print(f"正确答案 {i*j}")

        print('--'*10)
        n = n+1
        if n > limit:
            print('测试结束........')
            return


# dededed
# todo dedede
# test1(t=2, limit=5)
test3(t=5, limit=30)
