from bisect import bisect_left


def climb_stairs(n):
    """Ways to climb n steps taking 1 or 2 at a time. Fibonacci DP, O(n) time, O(1) space."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def coin_change(coins, amount):
    """Fewest coins to make amount, or -1. Bottom-up DP, O(amount * len(coins))."""
    inf = amount + 1
    dp = [0] + [inf] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != inf else -1


def length_of_lis(nums):
    """Longest increasing subsequence via patience sorting, O(n log n)."""
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
