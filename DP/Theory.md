## Basic of Dynamic programming 


* The core component of DP is Recursion and we need overlapping subproblems to use DP, which occur during recursive calls.
* There are 2 ways to perform DP 
    * **Memoization**: Where we cache the outputs of sub-problems to use for solving another sub problem 
    * **Tabulation:** In which we use loop rather than recursive function to run the code, further we can space optimize if possible in this, using some brain storming. 

## Below is the example code of Fibonacci Solved using recursion, memoization and tabulation. 

```python 
class Fib:
    def fib_tabulation(self,dp,n):
        dp[0] = 0 
        dp[1] = 1 
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    def fib_tab_space_opt(self,n):
        l = 0 
        r = 1 
        for i in range(2,n+1):
            j = l + r 
            l = r 
            r = j 
        return r 
    def fib_memo(self,dp_map,num):
        # top down approach
        if num <= 1:
            return num
        if dp_map[num] != -1:
            return dp_map[num]

        dp_map[num] = self.fib_memo(dp_map,num-1) + self.fib_memo(dp_map,num-2)
        return dp_map[num]
    def fibonacci(self,num):
        # base case 
        if num <= 0 or num == 1:
            return num

        return self.fibonacci(num-1) + self.fibonacci(num-2)
```
