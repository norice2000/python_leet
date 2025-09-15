from typing import List, Dict
import time

def coin_change_fast(amount, coins, memo=None):
    # Create memo dictionary
    if memo is None:
        memo = {}
    
    # 🎯 CHECK MEMO FIRST!
    if amount in memo:
        return memo[amount]  # Already solved!
    
    # Base cases
    if amount == 0:
        memo[amount] = 0  # Save base case
        return 0
    if amount < 0:
        return float('inf')
    
    # Try each coin
    min_coins = float('inf')
    for coin in coins:
        if coin <= amount:
            result = coin_change_fast(amount - coin, coins, memo)
            if result != float('inf'):  # Only update if valid result
                min_coins = min(min_coins, result + 1)
    
    # 💾 SAVE RESULT BEFORE RETURNING!
    memo[amount] = min_coins
    return min_coins

coins = (1, 5, 10)
amount = 11
print(coin_change_fast(amount, coins))  # ✅ CORRECT: amount first, coins second