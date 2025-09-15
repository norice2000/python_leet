from typing import List, Union, Any
from dataclasses import dataclass
import json

def min_coins_needed(coins: List[int], amount: int) -> int:
    """
    CHALLENGE 6: Minimum Coin Change - Australian Currency
    
    Given Australian coin denominations and an amount, find the minimum 
    number of coins needed to make that amount.
    
    Args:
        coins: List of coin denominations [5, 10, 20, 50, 100, 200] cents
        amount: Target amount in cents
    
    Returns:
        Minimum number of coins needed, or -1 if impossible
    
    Example:
        coins = [5, 10, 20, 50, 100, 200], amount = 30
        Result: 2 (20 + 10 = 30 cents, using 2 coins)
        
        coins = [5, 10, 20, 50, 100, 200], amount = 43
        Result: -1 (impossible - no combination adds to 43)
        
        coins = [5, 10, 20, 50, 100, 200], amount = 280
        Result: 2 (200 + 50 + 30 = 280, but 30 needs 20+10, so total = 4 coins)
        Actually: 200 + 50 + 20 + 10 = 280 (4 coins)
    
    Real-world: Point-of-sale systems calculating change,
    vending machine coin dispensing, payment processing optimization
    """
    # TODO: Dynamic Programming approach
    coins.sort()
    memo = {0:0}

    def min_coins(amnt):
        if amnt in memo:
            return memo[amnt]
        
        minn = float('inf')
        for coin in coins:
            diff = amnt - coin
            if diff < 0:
                break
            minn = min(minn, 1 + min_coins(diff))

        memo[amnt] = minn
        return minn
    result = min_coins(amount)
    if result < float('inf'):
        return result
    else:
        return -1

coins = [5, 10, 20, 50, 100, 200], amount = 30
print(min_coins_needed(coins, amount))