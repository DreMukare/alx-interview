#!/usr/bin/python3
'''solves the making change problem'''


def makeChange(coins, total):
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    if dp[total] != (total + 1):
        return dp[total]
    return -1
