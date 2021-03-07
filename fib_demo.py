'''
Date: 2021-03-08 05:31:43
LastEditTime: 2021-03-08 06:33:02
Author: Ye-P
Descripttion: 斐波那契数列的平凡解法
'''


def fib1(n):
    """
    斐波拉起暴力递归，算法复杂度为指数函数爆炸，2^n
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


def fib2(n):
    """
    算法复杂度降低为n
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = 0
    cure = 1
    for i in range(1, n):
        sumn = cure+prev
        prev = cure
        cure = sumn
    return cure


def fib3(n):
    "带备忘录的解法"
    memo = dict()

    def f(n):
        if memo.get(n):
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        sub = f(n-1)+f(n-2)
        memo[n] = sub
        return sub

    return f(n)


n = 100
print(fib2(n))
print(fib3(n))
