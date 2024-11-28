#!/usr/bin/python3
"""
making change module
"""

def makeChange(coins, total):
    """
    makeChange method
    """
    # If total is less than or equal to 0, return 0 (no coins needed)
    if total <= 0:
        return 0
 
    # Initialize the dp array with infinity, and dp[0] = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
  
    # Loop through each coin
    for coin in coins:
        # Update the dp array for every amount from the coin value to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means it's not possible to make the total
    return dp[total] if dp[total] != float('inf') else -1
