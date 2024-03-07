def max_profit(prices):
    n = len(prices)
    k = 2  # Maximum allowed transactions

    # Initialize a 2D array to store maximum profit
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_diff = -prices[0]  # Initialize max_diff for each transaction
        for i in range(1, n):
            dp[t][i + 1] = max(dp[t][i], prices[i] + max_diff)
            max_diff = max(max_diff, dp[t - 1][i] - prices[i])

    return dp[k][n]

# Test cases
test_cases = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [10, 22, 5, 75, 65, 80],
    [2, 30, 15, 10, 8, 25, 80],
    [10, 22, 5, 75, 65, 80]
]

for prices in test_cases:
    print(f"Input: {prices}")
    print(f"Output: {max_profit(prices)}")
    print()
