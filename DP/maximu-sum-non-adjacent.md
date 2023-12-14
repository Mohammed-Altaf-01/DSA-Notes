## Problem Statement 
we are given an array `nums` of integers, and we have the return the maximum sum of the integers but with the constraint that no two elements are adjacent in the given array 

example 1:
size = 5
nums = 1 2 3 5 4

output = 8 

example 2: 
size = 3
nums = 1 2 4 

output = 5

```Python 
# recursive solution 
# exponential TC 
def recur(nums,n,i):
    # base case 
    if i >= n:
        return 0 

    inc = recur(nums,n,i+2) + nums[i]
    exc = recur(nums,n,i+1)
    return max(inc,exc)
```

```python 
# recursion with memoization 
# O(N) - TC with O(N + N) ~ O(N) - SC
def recur_memo(nums,n,i,dp):
    # base case 
    if i >= n:
        return 0 
    if dp[i] != -1:
        return dp[i]
    
    inc = recur_memo(nums,n,i+2,dp) + nums[i]
    exc = recur_memo(nums,n,i+1,dp)
    dp[i] = max(inc,exc)
    return dp[i]

```
```python 
# tabulation with space optimized 
# O(N) TC and  O(1) - SC
def tabulation(nums,n):
    prev2 = 0 
    prev1 = nums[0]
    for i in range(1,n):
        inc = nums[i] + prev2
        exc = prev1

        cur = max(inc,exc)
        prev2 = prev1 
        prev1 = cur 
    return prev1
```