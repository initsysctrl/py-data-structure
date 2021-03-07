'''
Date: 2021-03-08 06:11:50
LastEditTime: 2021-03-08 06:24:12
Author: Ye-P
Descripttion: 凑硬币问题
'''


from typing import List


def coin_change(coins: List[int], amount: int):
    memo = dict()

    def dp(n):
        if n in memo:
            return memo[n]
        if n < -1:
            return -1
        if n == 0:
            return 0
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n-coin)
            if sub_problem == -1:
                continue
            res = min(res, sub_problem+1)
        if res == float('INF'):
            memo[n] = -1
        else:
            memo[n] = res
        return memo[n]
    return dp(amount)
def coinChange(coins: List[int], amount: int):
    # 备忘录
    memo = dict()
    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)

print(coin_change([1, 2, 5], 11))
print(coinChange([1, 2, 5], 11))
