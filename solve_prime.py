'''
Date: 2021-03-11 07:26:19
LastEditTime: 2021-03-12 05:13:27
Author: Ye-P
Descripttion: 编写出求两正整数M,N之间的最大公因数的程序
'''


def solve_prime(m: int, n: int) -> int:
    """求最大公因数

    Arguments:
        m {int} -- [数A]
        n {int} -- [数B]

    Returns:
        int -- [因数]
    """
    x = min(m, n)
    for i in reversed(range(1, x+1)):
        if m % i == 0 and n % i == 0:
            return i
        else:
            continue
    return 1


r = solve_prime(1024, 512)
print(r)