You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

* For this problem I have not understood the tabulation solution so I have not written it here. 

```python 
# recursive solution with exponential time complexity.
    def recur(self,coins,amount,dp):
        # base case 
        if amount == 0:
            return 0 
        if amount < 0:
            return float("inf")
        
        cnt = float('inf')
        for i in range(len(coins)):
            cur = self.recur(coins,amount-coins[i],dp)
            if cur != float('inf'):
                cnt = min(cnt,cur+1)
        return cnt 
```
```python 
    from collections import defaultdict
# top down approach with memoization. 
    def recur(self,coins,amount,dp):
        # base case 
        if amount == 0:
            return 0 
        if amount < 0:
            return float("inf")
        
        if dp[amount] != -1:
            return dp[amount]
        
        cnt = float('inf')
        for i in range(len(coins)):
            cur = self.recur(coins,amount-coins[i],dp)
            if cur != float('inf'):
                cnt = min(cnt,cur+1)
        dp[amount] = cnt
        return cnt 

```