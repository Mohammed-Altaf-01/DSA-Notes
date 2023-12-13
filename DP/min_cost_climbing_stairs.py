'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

# recursive solution with exponential TC and recursive stack space 
def recur(cost,idx,n):
    # base case 
    if idx >= n:
        return 0 
    # recursive relation 
    return cost[idx] + min(self.recur(cost,idx+1,n),self.recur(cost,idx+2,n))

# recursion for memoization solution 
# TC - O(N)
# SC - O(N) for dp and O(N) for recursive stack
def dp_sol(cost,idx,n,dp):
    # base case 
    if idx >= n:
        return 0 
    
    # return cached values
    if dp[idx] != -1:
        return dp[idx]
    
    # cahce sub problems output
    dp[idx] = cost[idx] + min(self.dp_sol(cost,idx+1,n,dp),self.dp_sol(cost,idx+2,n,dp))
    return dp[idx]

# tabulation with space optimized 
def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    a = cost[0]
    b = cost[1]

    for i in range(2,n):
        cur = cost[i] + min(a,b)
        a = b 
        b = cur 
    # ouput is calculated as a sum so return min between two values
    return min(a,b)
    




         