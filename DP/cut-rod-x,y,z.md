## problem statement 

You are given a integer N denoting the length of the rod. You need to determine the maximum number of segments you can make of this rod provided tha each segment should be of the length X or Y or Z 

Sample Input 1:
2
7 5 2 2
8 3 3 3
Sample Output 1:
2
0

In the first test case, cut it into 2 parts of 5 and 2.

In the second case, there is no way to cut into segments of 3 length only as the length of the rod is less than the given length. 

```python
# recursion solution
def recur(size,x,y,z):
    # base cases 
    if size < 0 :
        return float('inf')
    if size == 0:
        return 0

    max_segment = float('-inf')
    for cut in [x,y,z]:
        cur_segment =  recur(size-cut,x,y,z)
        if cur_segment != float('inf'):
            max_segment = max(max_segment,cur_segment+1)
    return max_segment
```


```python
# recursion with memoization 
def memoized(size,x,y,z,dp):
    # base case 
    if size < 0:
        return float('inf')
    if size == 0:
        return 0 
    
    if dp[size] != -1:
        return dp[size]
    
    max_seg = float('-inf')
    for cut in [x,y,z]:
        cur_segment = memoized(size-cut,x,y,z,dp)
        if cur_segment != float('inf'):
            max_seg = max(max_seg,cur_segment+1)
    dp[size] = max_seg
    return dp[size]
```
# I got stuck at tabulation solution learn a more about it and again build the tabulation solution 
